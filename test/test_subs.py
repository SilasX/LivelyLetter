from json import JSONDecoder
from os.path import dirname, join
import unittest
from PyvelyLetter.model import Letter

THIS_DIR = dirname(__file__)
SAMPLE_NUM = 1000

class TestSingleSubs(unittest.TestCase):

    def setUp(self):
        super(TestSingleSubs, self).setUp()
        with open(join(THIS_DIR, "json1_letter.txt"), "r") as f:
            self.text = f.read().strip()
        with open(join(THIS_DIR, "input_dict.json"), "r") as f:
            self.subs_dict = JSONDecoder().decode(f.read())
        self.ltr_obj = Letter(self.text, self.subs_dict)

    def tearDown(self):
        super(TestSingleSubs, self).tearDown()

    def test_const_letter(self):
        with open(join(THIS_DIR, "const_letter.txt"), "r") as f:
            text = f.read().strip()
        ltr_obj = Letter(text)
        expected = "Hello World."
        actual = ltr_obj.apply_subs(is_random=False)
        self.assertEqual(expected, actual)

    def test_one_choice_subs(self):
        expected = "Howdy,\nGood to see you."
        actual = self.ltr_obj.apply_subs(is_random=False)
        self.assertEqual(expected, actual)

class TestMultiSubs(unittest.TestCase):

    def setUp(self):
        super(TestMultiSubs, self).setUp()
        with open(join(THIS_DIR, "json2_letter.txt"), "r") as f:
            self.text = f.read().strip()
        with open(join(THIS_DIR, "input_dict.json"), "r") as f:
            self.subs_dict = JSONDecoder().decode(f.read())
        self.ltr_obj = Letter(self.text, self.subs_dict)
        self.template = "{{salutation}},\nGood to see you.\n{{ending}}"

    def tearDown(self):
        super(TestMultiSubs, self).tearDown()

    def test_multi_choice(self):
        expecteds = []
        for x in ["Howdy", "Hi"]:
            for y in ["Bye.", "See you soon."]:
                version = self.text.replace("{{salutation}}", x)
                version = version.replace("{{ending}}", y)
                expecteds.append(version)
        actuals = [self.ltr_obj.apply_subs() for i in xrange(SAMPLE_NUM)]
        self.assertTrue(all(expected in actuals for expected in expecteds))

    def test_permutation_count(self):
        """probabilistic test"""
        expected = 4
        ltr_obj = Letter(self.text, self.subs_dict)
        uniq_ltrs = set()
        for i in xrange(SAMPLE_NUM):
            uniq_ltrs.add(ltr_obj.apply_subs())
        actual = len(uniq_ltrs)
        self.assertEqual(expected, actual)

