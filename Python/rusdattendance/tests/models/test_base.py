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
