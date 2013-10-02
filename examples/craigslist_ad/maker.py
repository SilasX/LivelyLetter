from json import JSONDecoder
from random import sample

from LivelyLetter import Letter


class CLAd(object):
    pass

def random_string(s):
    return sample(s.split(), 1)[0]

ad_obj = CLAd()
ad_obj.url = "http://example.com/craigslistadd_325"
ad_obj.name = "Jake"
ad_obj.text = """Get this 500 sq ft apartment for only $3000/month.  Only a 30 minute walk from public transit.  A steal for San Francisco!
"""
ad_obj.blah = random_string(ad_obj.text)

with open("templates/temp1.txt", "r") as f:
    letter_temp = f.read().strip()

with open("jsons/ad1.json", "r") as f:
    subs_dict = JSONDecoder().decode(f.read())

clad_dict = {
    'ad': ad_obj,
}

for x in range(3):
    my_letter = Letter(letter_temp, subs_dict)
    my_letter.apply_all()
    print my_letter.apply_objects(clad_dict, reset=False)
    print "######"
