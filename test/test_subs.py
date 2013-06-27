import os
import unittest
from PyvelyLetter.model import Letter

class TestSubs(unittest.TestCase):

    def setUp(self):
        super(TestSubs, self).setUp()

    def tearDown(self):
        super(TestSubs, self).tearDown()

    def test_const_letter(self):
        with open(os.path.join(os.path.dirname(__file__), "const_letter.txt"), "r") as f:
            text = f.read().strip()
        ltr_obj = Letter(text)
        expected = "Hello World."
        actual = ltr_obj.apply_subs()
        self.assertEqual(expected, actual)
