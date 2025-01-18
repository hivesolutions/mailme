#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


class BaseTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(1 + 1, 2)
