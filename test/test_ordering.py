from json import JSONDecoder
from os.path import dirname, join
import unittest

from PyvelyLetter.model import Letter

THIS_DIR = dirname(__file__)
SAMPLE_NUM = 1000


class TestTwoItemReverse(unittest.TestCase):

    def setUp(self):
        super(TestTwoItemReverse, self).setUp()

    def tearDown(self):
        super(TestTwoItemReverse, self).tearDown()

    def test_start_and_end(self):
        """test for case when re-orderable strings are only at start and end"""
        expected = 2
        with open(join(THIS_DIR, "ordering_letter1.txt"), "r") as f:
            text = f.read().strip()
        ltr_obj = Letter(text)
        uniq_ltrs = set()
        for i in xrange(SAMPLE_NUM):
            uniq_ltrs.add(ltr_obj.apply_ordering())
        actual = len(uniq_ltrs)
        self.assertEqual(expected, actual)
