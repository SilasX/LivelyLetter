#### LivelyLetter
This is a system for making form letters with more variety, realism, and a human touch.

#### Installation

Inside your `virtualenv` environment (you [use that](http://www.virtualenv.org/en/latest/), right?), run:

    pip install git+git://github.com/SilasX/LivelyLetter.git

Then you'll be able to import the LivelyLetter module in all its pythonic goodness.  See "Generating a version of the letter".

#### Features

##### Simple Substitutions from dictionary
Given:
a) an input file template, and  
b) a (for example) JSON file with the substitutions you want to make into the letter template,

output a form letter with substitutions from the JSON file. The JSON entries can be arrays, in which case it makes the substitution with a randomly-chosen member of the array.

In your input form letter template, surround every variable with `{{` and `}}` that you want to substitute from the JSON, and then ensure it corresponds to a string entry with the same key in your JSON file. For example, if you have {{name}}, in your form letter template (FLT), make sure you have a line like 

    "name": "Bobby",

somewhere in your JSON file.

##### Substitutions of a random string from JSON
Given:
a) an input file template as before, and  
b) a JSON file with containing arrays of possible values for each key such that you want one of the values substituted in,

output a form letter that uses one of the possible values at each key/array instances.

For example, if you have `{{salutation}}` in your form letter, and an entry in your JSON file like

    "salutation": ["Hi", "Howdy", "Good day"],

then one of those three values (`Hi`, `Howdy`, or `Good day`) will be substituted into the ``{{salutation}}`` string instances of the letter.

##### Substitutions based on object methods.

Got your own funky ideas for what to swap out in?  No problem!  You can tell the template to substitute into the letter based on given objects and methods. Just mark the place for the substitution in the form `[[# object_string#method #]]` and pass in a dictionary mapping all `object_string`s to object variables.  For example, if your template looks like this (stored in the `text` variable):

    Jane, I like how you mentioned [[# discussion#topic #]]. You
    spent a full [[# discussion#word_count #]] words on it!

Then you just need to make sure you have a `discussion` object defined, and you can apply the object methods as so:

    ltr_obj = Letter(text=text)
    output_letter = ltr_obj.apply_objects({
        'discussion': discussion,
    })

In the example above, you would need to make sure that the `discussion` object returns something when `.topic` and `.word_count` are called on it.

##### Random re-ordering of indicated sections.

You can mark certain sections as being re-orderable, and LivelyLetter with pick a random ordering for them. (Note: this does not require a dictionary object as input, as the template contains all information necessary to do it.)

For example, let's say you use "Shalom" for both a greeting and a closing, and the same for "Good Day".  You then place one of each at the begining and end of the file.  Surround the text you want to appear in `[[ ]]` on each of them and prepend a label to the ground surrounded in `[# #]`.  Here is what the template would look like:

    [#gtg_grp#][[Shalom]], John.
    I would like to subscribe to your newsletter.
    [#gtg_grp#][[Good day]].

The `[#gtg_grp#]` indicates that the strings are part of the same reorderable group.  (`gtg_grp` is arbitrary.)

When it generates an instance of a letter, it will either begin with `Shalom` and end with `Good day` or vice versa, chosen at random.

#### Generating a version of the letter

Why, it's as easy as gettin' your Border Collie out of the farmhouse for some sheep-herdin'.

##### 1) import the Letter object
    from LivelyLetter import Letter

##### 2) bring in a file (JSON shown) as a dictionary for the substitution
    from json import JSONDecoder
    with open("my_subs.json", "r") as f:
        subs_dict = JSONDecoder().decode(f.read())

##### 3) bring in a text file as the template to apply the substitutions fo
    with open("form_letter.txt", "r") as f:
        letter_text = f.read().strip()

##### 4) Initialize the letter object
    my_letter = Letter(letter_text, subs_dict)

##### 5) Generate a version and store in variable -- repeat as necessary
    letter_version = my_letter.apply_all()

#### Miscellaneous
This project will eventually be extended to allow for randomly ordering the sections of the letter. 

Don't use this for spam.  Seriously -- not cool.

Code as hosted on Github is released under the MIT license.  You know where to find it. 

