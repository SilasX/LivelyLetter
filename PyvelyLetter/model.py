from random import choice


class Letter(object):

    def __init__(self, text="", subs_dict=None):
        self.text = text
        self.subs_dict = subs_dict
        # markers for substitution
        self.begin_delimiter = "{{"
        self.end_delimiter = "}}"
        # markers for re-orderable groups
        self.begin_orderable = "["
        self.end_orderable = "]"

    def apply_subs(self, is_random=True):
        output = self.text
        if self.subs_dict:
            for key, value in self.subs_dict.iteritems():
                repl_from = self.begin_delimiter + str(key) + self.end_delimiter
                if hasattr(value, '__iter__'):
                    if is_random:
                        repl_to = choice(value)
                    else:
                        repl_to = value[0]
                else:
                    repl_to = value
                output = output.replace(repl_from, repl_to)
        return output

    def apply_ordering(self):
        output = self.text

