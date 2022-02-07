# Copyright (C) 2022 by Higher Expectations for Racine County
r"""The base class for data model classes."""

from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import (
    declared_attr,
    declarative_mixin,
    relationship,
)


from rusdattendance.models.base import Base


class Label(Base):
    r"""String representations that may vary across years."""
    __tablename__ = 'labels'
    text = Column(String,
                  unique=True,
                  nullable=False)

    def __repr__(self):
        return '<Label: "%s">' % self.text


#@declarative_mixin
# class LabeledMixin:
#     r"""A class that may have multiple text labels for identical instances."""
#
#     @declared_attr
#     def preferred_label(cls):
#         return Column(Integer,
#                       ForeignKey('labels.id'))
#
#     @declared_attr
#     def _label_association(cls):
#         r"""this may need to save the `Table` as a class data member."""
#         table_name = cls.__tablename__
#         return Table(f'{table_name}_labels',
#                      Base.metadata,
#                      Column(f'{table_name}_id',
#                             ForeignKey(f'{table_name}.id'),
#                             primary_key=True),
#                      Column('label_id',
#                             ForeignKey(f'{Label.__tablename__}.id'),
#                             primary_key=True),
#                      )
#
#     @declared_attr
#     def labels(cls):
#         r"""I am hoping that this function implicitly saves the association table."""
#         return relationship('Label',
#                             secondary=cls._label_association)
