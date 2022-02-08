# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Tests for a generic Label table for any multi-value text columns."""

import pytest

from sqlalchemy import (
    select,
    Column,
    Integer,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import (
    selectinload
)

from rusdattendance.models.base import Base

from rusdattendance.models.labels import (
    Label,
    LabeledMixin,
)


@pytest.fixture(scope='module')
def label_texts():
    r"""three text values for labels."""
    return [
        'foo',
        'bar',
        'baz'
    ]


class LabeledDummy(LabeledMixin, Base):
    r"""we'll see if this works."""
    __tablename__ = 'labelled_dummy'

    value = Column(Integer)

    def __repr__(self):
        return '<Dummy "%s": %d (%s)' % (
            self.preferred_label.text,
            self.value,
            ', '.join([x.text for x in self.labels])
        )

@pytest.fixture(scope='module')
def label_engine(engine):
    r"""An engine that knows about the Label class."""
    engine.add_model_to_engine(LabeledDummy)
    engine.add_model_to_engine(Label)
    return engine


@pytest.fixture(scope='module')
def preloaded_labels(label_engine,
                     label_texts):
    r"""preload some labels into the database. i hope..."""

    with label_engine.session() as session:
        session.add_all([Label(text=x) for x in label_texts])
        session.commit()

    return label_texts


def test_label(label_engine,
               preloaded_labels):
    r"""Instantiation creates text and an empty id"""

    label_query = select(Label)

    with label_engine.session() as session:
        labels = session.execute(label_query).scalars()
        for i, (text, label) in enumerate(zip(preloaded_labels, labels)):
            assert label.text == text
            assert label.id == i + 1


def test_no_null_label_text(label_engine):
    r"""Label texts cannot be `None`"""

    with label_engine.session() as session:
        foo = Label(text=None)
        assert foo.text is None
        session.add(foo)
        with pytest.raises(IntegrityError) as exc_info:
            session.flush()

    assert str(exc_info.value) == ('(sqlite3.IntegrityError) NOT NULL constraint failed: labels.text\n'
                                   '[SQL: INSERT INTO labels (text) VALUES (?)]\n'
                                   '[parameters: (None,)]\n'
                                   '(Background on this error at: https://sqlalche.me/e/14/gkpj)')


def test_no_duplicate_label_text(label_engine,
                                 preloaded_labels):
    r"""Label texts must be unique."""

    with label_engine.session() as session:
        foo = Label(text=preloaded_labels[0])
        assert foo.text == preloaded_labels[0]
        session.add(foo)
        with pytest.raises(IntegrityError) as exc_info:
            session.flush()

    assert str(exc_info.value) == ('(sqlite3.IntegrityError) UNIQUE constraint failed: labels.text\n'
                                   '[SQL: INSERT INTO labels (text) VALUES (?)]\n'
                                   f"[parameters: ('{preloaded_labels[0]}',)]\n"
                                   '(Background on this error at: https://sqlalche.me/e/14/gkpj)')


def test_labeled_mixin(label_engine,
                       preloaded_labels):
    r"""i don't even know if the session will work"""

    label_query = select(Label)
    with label_engine.session() as session:
        labels = session.execute(label_query).scalars().all()
        dummy = LabeledDummy(value=42,
                             preferred_label=labels[0],
                             labels=labels)
        session.add(dummy)
        session.add_all([
            Label(text='not included'),
            Label(text='in dummy'),
        ])
        labels = session.execute(label_query).scalars().all()
        session.add(LabeledDummy(value=-1,
                                 preferred_label=labels[-3],
                                 labels=labels[-3:]))
        idiots = session.execute(
            select(LabeledDummy).options(selectinload(LabeledDummy.labels))
        ).scalars().all()

    assert idiots[0].preferred_label == labels[0]
    assert idiots[0].labels == labels[:3]

    assert idiots[1].preferred_label == labels[2]
    assert idiots[1].labels == labels[-3:]

    for idiot in idiots:
        assert idiot.preferred_label == idiot.labels[0]
