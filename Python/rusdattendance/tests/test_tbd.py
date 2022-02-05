# Copyright (C) 2022 by Higher Expectations for Racine County

import pytest

from tbd import (
    documented,
    vetted,
)


@pytest.mark.parametrize('param',
                         [
                             'World',
                             'Nurse',
                             'Felicia',
                         ])
def test_documented(param):
    r"""The input should be greeted."""

    assert documented(param) == f'Personalized greetings to you, {param}!'


@pytest.mark.parametrize('param',
                         list(range(9, 22)))
def test_vetted(param):
    r"""We're just multiplying by three here."""

    assert vetted(param) == 3 * param
