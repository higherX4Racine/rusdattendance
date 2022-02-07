# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Tables that directly pertain to school activity"""

from sqlalchemy import (
    Column,
    ForeignKey,
    Boolean,
    Date,
    Float,
    Integer,
)

from rusdattendance.models.base import Base
from rusdattendance.models.labels import LabeledMixin


class GradeLevel(LabeledMixin, Base):
    r"""A specific grade level like Kindergarten or High School Senior."""
    __tablename__ = 'grade_level'
    order = Column(Integer,
                   unique=True,
                   nullable=False)


class Tier(LabeledMixin, Base):
    r"""A category of school, like elementary or middle."""
    __tablename__ = 'tier'
    lower_grade_level = Column(Integer,
                               ForeignKey('grade_level.id'))
    upper_grade_level = Column(Integer,
                               ForeignKey('grade_level.id'))


class School(LabeledMixin, Base):
    r"""A location/institution where instruction occurs."""
    __tablename__ = 'school'
    tier = Column(Integer,
                  ForeignKey('tier.id'))


class Enrollment(Base):
    r"""One student, one school, one year"""

    __tablename__ = 'enrollment'

    student = Column(Integer,
                     ForeignKey('student.id'))

    school = Column(Integer,
                    ForeignKey('school.id'))

    start_date = Column(Date)
    end_date = Column(Date)

    special_education = Column(Boolean)

    scheduled_days = Column(Integer)

    days_absent = Column(Float)
