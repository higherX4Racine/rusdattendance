# Copyright (C) 2022 by Higher Expectations for Racine County
r"""The base class for data model classes."""

from sqlalchemy import (
    Column,
    Integer,
)

from sqlalchemy.orm import (
    declarative_base,
)


class RootObject:
    r"""Every object has a primary key called "ID," defined here."""
    id = Column(Integer,
                primary_key=True)


Base = declarative_base(cls=RootObject)
