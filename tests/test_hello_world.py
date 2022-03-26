"""This file contains an example of unit testing in Python."""

import unittest

from project.hello_world import hello_world


class TestCase(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello World!")