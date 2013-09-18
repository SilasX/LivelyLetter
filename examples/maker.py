from json import JSONDecoder

from LivelyLetter import Letter


class Customer(object):

    def __init__(self, name):
        self.name = name

the_customers = [
    Customer("Alice"),
    Customer("Bob"),
]
with open("templates/temp1.txt", "r") as f:
    letter_temp = f.read().strip()

with open("jsons/json1.json", "r") as f:
    subs_dict = JSONDecoder().decode(f.read())

my_letter = Letter(letter_temp, subs_dict)
for cust in the_customers:
    obj_dict = {
        'customer': cust,
    }
    my_letter.apply_all()
    print my_letter.apply_objects(obj_dict, reset=False)
    print "############"
