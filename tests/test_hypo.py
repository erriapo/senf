# -*- coding: utf-8 -*-
# Copyright 2016 Christoph Reiter
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

import pytest

try:
    import hypothesis
    from hypothesis import given, strategies
except ImportError:
    hypothesis = None

from senf import fsnative, text2fsn, fsn2text, bytes2fsn, fsn2bytes
from senf._compat import text_type


if hypothesis:
    @given(strategies.text())
    def test_fsnative(text):
        assert isinstance(fsnative(text), fsnative)


    @given(strategies.text())
    def test_text2fsn(text):
        assert isinstance(text2fsn(text), fsnative)


    @given(strategies.text())
    def test_text_fsn_roudntrip(text):
        assert isinstance(fsn2text(text2fsn(text)), text_type)


    @given(strategies.binary(),
           strategies.sampled_from(("utf-8", "utf-16-le",
                                    "utf-32-le", "latin-1")))
    def test_bytes(data, encoding):
        try:
            path = bytes2fsn(data, encoding)
        except ValueError:
            pass
        else:
            assert fsn2bytes(path, encoding) == data