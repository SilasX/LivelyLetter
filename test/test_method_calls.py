from mock import Mock
from os.path import dirname, join
import unittest

from LivelyLetter.model import Letter

THIS_DIR = dirname(__file__)
SAMPLE_NUM = 1000


class TestMethodSubs(unittest.TestCase):

    def setUp(self):
        super(TestMethodSubs, self).setUp()

    def tearDown(self):
        super(TestMethodSubs, self).tearDown()

    def test_two_methods_on_object(self):
        expected = "Jane, I like how you mentioned widgets. You spent a full 206 words on it!"
        discussion = Mock()
        discussion.topic = "widgets"
        discussion.word_count = "206"
        with open(join(THIS_DIR, "method_letter_template.txt"), "r") as f:
            text = f.read().strip()
        ltr_obj = Letter(text=text)
        actual = ltr_obj.apply_objects({
            'discussion': discussion,
        })
        self.assertEqual(expected, actual)
