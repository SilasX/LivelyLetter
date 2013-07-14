from json import JSONDecoder
from os.path import dirname, join
import unittest
from PyvelyLetter.model import Letter

THIS_DIR = dirname(__file__)

class TestSubs(unittest.TestCase):

    def setUp(self):
        super(TestSubs, self).setUp()

    def tearDown(self):
        super(TestSubs, self).tearDown()

    def test_const_letter(self):
        with open(join(THIS_DIR, "const_letter.txt"), "r") as f:
            text = f.read().strip()
        ltr_obj = Letter(text)
        expected = "Hello World."
        actual = ltr_obj.apply_subs(is_random=False)
        self.assertEqual(expected, actual)

    def test_one_choice_subs(self):
        with open(join(THIS_DIR, "json1_letter.txt"), "r") as f:
            text = f.read().strip()
        with open(join(THIS_DIR, "input_dict.txt"), "r") as f:
            subs_dict = JSONDecoder().decode(f.read())
        expected = "Howdy,\nGood to see you."
        ltr_obj = Letter(text, subs_dict)
        actual = ltr_obj.apply_subs(is_random=False)
        self.assertEqual(expected, actual)

    def test_multi_choice(self):
        with open(join(THIS_DIR, "json1_letter.txt"), "r") as f:
            text = f.read().strip()
        with open(join(THIS_DIR, "input_dict.txt"), "r") as f:
            subs_dict = JSONDecoder().decode(f.read())
        expecteds = ["{{salutation}},\nGood to see you.".replace("{{salutation}}", x) for x in ["Howdy", "Hi"]]
        ltr_obj = Letter(text, subs_dict)
        actual = ltr_obj.apply_subs()
        self.assertTrue(actual in expecteds)
