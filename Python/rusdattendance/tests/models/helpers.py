# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Helper functions and classes for unit testing model classes"""

import sqlalchemy
from sqlalchemy.orm import Session


class HelperEngine:
    r"""Bundle the common database connection features used by `sqlalchemy`.

    Parameters
    ----------
    url : str
        The location of the test database

    """

    def __init__(self, url):
        self._url = url
        self._engine = sqlalchemy.create_engine(self.url)

    @property
    def url(self) -> str:
        r"""The location of the test database."""
        return self._url

    @property
    def engine(self):
        r"""A database engine."""
        return self._engine

    def add_model_to_engine(self, model_class):
        r"""Create all of the model class's tables.

        Parameters
        ----------
        model_class : type
            A class created with sqlalchemy declarative ORM

        """
        model_class.metadata.create_all(self.engine)

    def session(self):
        r"""A sqlalchemy session object in 2.0 format."""
        return Session(self.engine,
                       future=True)


