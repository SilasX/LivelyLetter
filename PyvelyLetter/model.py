from random import choice


class Letter(object):

    def __init__(self, text="", subs_dict=None):
        self.text = text
        self.subs_dict = subs_dict
        self.begin_delimiter = "{{"
        self.end_delimiter = "}}"
        #print self.begin_delimiter + "salutation" + self.end_delimiter

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
                # print (self.begin_delimiter + str(key) + self.end_delimiter, str(value))
        return output
