# Copyright (C) 2022 by Higher Expectations for Racine County

from sqlalchemy import (
    Column,
    Integer,
)
import pytest

from rusdattendance.models.base import Base


class Dummy(Base):
    __tablename__ = 'dummy'
    x = Column(Integer)


@pytest.mark.parametrize('value',
                         [1, 2, 3])
def test_base_initialization(value):
    r"""Does a base-inheriting object contain a primary key?"""

    d = Dummy(x=value)
    assert d.x == value
    assert d.id is None


def test_base_sessioning(sql_session_factory):
    r"""Committing should fill the ID """

    xes = list(range(40, 43))
    ids = list(range(1, 4))

    with sql_session_factory(Dummy) as session:
        session.add_all([Dummy(x=x) for x in xes])
        dummies = session.query(Dummy).order_by(Dummy.id).all()

    for d, x, i in zip(dummies, xes, ids):
        assert d.x == x
        assert d.id == i
