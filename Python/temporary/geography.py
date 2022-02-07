# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Tables that pertain to locations"""

from sqlalchemy import (
    Column,
    ForeignKey,
    Date,
    Integer,
    String,
)

from rusdattendance.models.base import Base


class Address(Base):
    r"""A physical location, for a school or a student."""

    __tablename__ = "address"

    number = Column(String)
    street = Column(String)
    tag = Column(String)
    prefix = Column(String)
    dir = Column(String)
    apartment = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    zip_plus_four = Column(Integer)


class Residency(Base):
    r"""A period of time when one student dwelt in one place."""

    __tablename__ = 'residency'

    student = Column(Integer,
                     ForeignKey('student.id'))

    address = Column(Integer,
                     ForeignKey('address.id'))

    start_date = Column(Date)
    end_date = Column(Date)
