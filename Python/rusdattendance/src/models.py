# Copyright (C) 2022 by Higher Expectations for Racine County
r"""SQLAlchemy table definitions. """

from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    Boolean,
    Date,
    Float,
    Integer,
    String,
)

from sqlalchemy.orm import (
    declared_attr,
    declarative_base,
    declarative_mixin,
    relationship,
)


class RootObject:
    r"""Every object has a primary key called "ID," defined here."""
    id = Column(Integer,
                primary_key=True)


Base = declarative_base(cls=RootObject)


class Label(Base):
    r"""String representations that may vary across years."""
    __table_name = 'labels'
    text = Column(String,
                  unique=True,
                  nullable=False)


@declarative_mixin
class LabeledMixin:
    r"""A class that may have multiple text labels for identical instances."""

    preferred_label = Column(Integer,
                             ForeignKey('labels.id'),
                             nullable=False)

    @declared_attr
    def _label_association(cls):
        r"""this may need to save the `Table` as a class data member."""
        table_name = cls.__tablename__
        return Table(f'{table_name}_labels',
                     Base.metadata,
                     Column(f'{table_name}_id',
                            ForeignKey(f'{table_name}.id'),
                            primary_key=True),
                     Column('label_id',
                            ForeignKey(f'{Label.__tablename__}.id'),
                            primary_key=True),
                     )

    @declared_attr
    def labels(cls):
        r"""I am hoping that this function implicitly saves the association table."""
        return relationship('Label',
                            secondary=cls._label_association(),
                            back_populates=cls.__tablename__)


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


class Address(Base):
    r"""A physical location, for a school or a student."""
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


class Enrollment(Base):
    r"""One student, one school, one year"""

    __tablename__ = 'enrollment'

    student = Column(Integer,
                     ForeignKey('student.id'))

    school = Column(Integer,
                    ForeignKey('school.id'))

    start_date = Column(Date)
    end_date = Column(Date)

    grade = Column(Integer,
                   ForeignKey('grade_level.id'))

    special_education = Column(Boolean)

    scheduled_days = Column(Integer)

    days_absent = Column(Float)
