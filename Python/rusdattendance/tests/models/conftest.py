# Copyright (C) 2022 by Higher Expectations for Racine

import pytest
from .helpers import (
    HelperEngine,
)


@pytest.fixture(scope='session',
                params=[
                    'sqlite:///:memory:',
                ])
def database_url(request):
    r"""The URL for a test database."""
    return request.param


@pytest.fixture(scope='module')
def engine(database_url):
    r"""A handler for a test database."""
    return HelperEngine(database_url)
