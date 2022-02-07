# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Tests for a generic Label table for any multi-value text columns."""

import pytest

from sqlalchemy.exc import IntegrityError

from rusdattendance.models.labels import Label


def test_label():
    r"""Instantiation creates text and an empty id"""
    label = Label(text='hello, world')
    assert label.text == 'hello, world'
    assert label.id is None


def test_label_sessioning(sql_session_factory):
    r"""some integrity issues can be tested here."""

    with sql_session_factory(Label) as session:
        foo = Label(text=None)
        session.add(foo)

        with pytest.raises(IntegrityError) as exc_info:
            session.flush()

        session.rollback()

        assert str(exc_info.value) == ('(sqlite3.IntegrityError) NOT NULL constraint failed: labels.text\n'
                                       '[SQL: INSERT INTO labels (text) VALUES (?)]\n'
                                       '[parameters: (None,)]\n'
                                       '(Background on this error at: https://sqlalche.me/e/14/gkpj)')

        bar = Label(text='barf')
        session.add(bar)
        session.commit()

        barf = Label(text='barf')

        session.add(barf)
        with pytest.raises(IntegrityError) as exc_info:
            session.flush()

        assert str(exc_info.value) == ('(sqlite3.IntegrityError) UNIQUE constraint failed: labels.text\n'
                                       '[SQL: INSERT INTO labels (text) VALUES (?)]\n'
                                       "[parameters: ('barf',)]\n"
                                       '(Background on this error at: https://sqlalche.me/e/14/gkpj)')
        session.rollback()

        labels = session.query(Label).all()
        assert len(labels) == 1
