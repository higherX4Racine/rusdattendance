# Copyright (C) 2022 by Higher Expectations for Racine

import pytest
import sqlalchemy
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope='module')
def sql_engine():
    r"""An in-memory SQLite database."""
    engine = sqlalchemy.create_engine('sqlite:///:memory:')
    yield engine
    del engine


@pytest.fixture(scope='module')
def sql_session_factory(sql_engine):
    r"""makes sessions tied to the engine."""
    session_factory = sessionmaker(bind=sql_engine)

    def _session(cls):
        cls.metadata.create_all(sql_engine)
        return session_factory()

    return _session
