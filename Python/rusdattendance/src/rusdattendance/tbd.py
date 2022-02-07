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


r"""
def association_table(table_name: str) -> Table:
    ""Associate a class with the `Label` table.

    Parameters
    ----------
    table_name : str
        The name that the table will have, once it is built.

    Returns
    -------
    association_table : sqlalchemy.orm.Table
        A `Table` with fields that reference the primary keys of two others.

    ""

    return Table(f'{table_name}_labels',
                 Base.metadata,
                 Column(f'{table_name}_id',
                        ForeignKey(f'{table_name}.id'),
                        primary_key=True),
                 Column('label_id',
                        ForeignKey(f'{Label.__tablename__}.id'),
                        primary_key=True),
                 )


grade_level_labels = association_table('grade_level')

"""