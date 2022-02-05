# Copyright (C) 2022 by Higher Expectations for Racine County
r"""This is a stub for working out `sphinx` and `pytest` in PyCharm"""


def documented(greeted_party: str) -> str:
    r"""A "Hello, world!" variation to test autodocumentation.

    Parameters
    ----------
    greeted_party : str
       This will be the object of the greeting

    Returns
    -------
    greeting : str
        a personalized greeting

    """

    return f'Personalized greetings to you, {greeted_party}!'


def vetted(factor: int) -> int:
    r"""A multiplication variation to test unit testing.

    Parameters
    ----------
    factor : int
        This number will be multiplied by three.

    Returns
    -------
    result : int
        three times the factor

    """

    return 3 * factor
