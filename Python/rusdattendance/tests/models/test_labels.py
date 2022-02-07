# Copyright (C) 2022 by Higher Expectations for Racine County
r"""Tests for a generic Label table for any multi-value text columns."""

from rusdattendance.models.labels import Label


def test_label():
    label = Label(text='hello, world')
    assert label.text == 'hello, world'
    assert label.id is None
