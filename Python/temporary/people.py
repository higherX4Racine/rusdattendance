# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Tables directly pertaining to a person's identity."""

from sqlalchemy import (
    Column,
    ForeignKey,
    Boolean,
    Date,
    Integer,
)

from rusdattendance.models.base import Base
from rusdattendance.models.labels import LabeledMixin


class Race(LabeledMixin, Base):
    r"""The race of a student."""
    __tablename__ = 'race_or_ethnicity'
    federal_code = Column(Integer,
                          unique=True)


class Gender(LabeledMixin, Base):
    r"""Usually actually the birth sex, rather than the actual gender."""
    __tablename__ = 'gender'


class Language(LabeledMixin, Base):
    r"""The primary language that a student interacts with at home."""
    __tablename__ = 'language'


class Student(Base):
    r"""Identity and demographic information about one student."""
    __tablename__ = 'student'

    student_number = Column(Integer,
                            unique=True,
                            nullable=False)

    birthdate = Column(Date)

    gender = Column(Integer,
                    ForeignKey('gender.id'))

    race = Column(Integer,
                  ForeignKey('race_or_ethnicity.id'),
                  nullable=False)

    latinx = Column(Boolean,
                    nullable=False)

    language = Column(Integer,
                      ForeignKey('language.id'))
