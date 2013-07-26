import re

from random import choice, randint


class Letter(object):

    def __init__(self, text="", subs_dict=None):
        self.text = text
        self.subs_dict = subs_dict
        # markers for substitution
        self.begin_delimiter = "{{"
        self.end_delimiter = "}}"
        # regexes for group names and contents (orderables)
        self.group_name_start = r'\[#'
        self.group_name_end = r'#\]'
        self.group_pat_start = r'\[\['
        self.group_pat_end = r'\]\]'
        self.set_regexes()  # define all member vars that use the above four
        self.partition()

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

    def partition(self):
        """create the self.order_groups member variable to prepare for ordering theletter"""
        group_pattern = re.compile(self.group_pattern_re)
        group_pattern_cpd = re.compile(self.group_pattern_cpd_re)
        self.order_groups = {}
        # get patterns in the form [ (group name, text) ... ]
        parsed_groups = re.findall(group_pattern_cpd, self.text)
        # print parsed_groups
        for x in parsed_groups:
            this_gp_pattern = self.group_name_start + x[0] + self.group_name_end + self.orderable_re
            if this_gp_pattern in self.order_groups:
                self.order_groups[this_gp_pattern].append(x[1])
            else:
                self.order_groups[this_gp_pattern] = [x[1]]

    def apply_ordering(self):
        """return the result of applying a random ordering to the orderable parts """
        output = self.text
        # iterate over each key/pattern in self.order_groups, replacing until no more texts to apply
        order_dict = self.order_groups
        for pattern in order_dict:
            print "working " + str(pattern)
            while order_dict[pattern] != []:
                print "remaining texts are " + str(order_dict[pattern])
                # get a random index from the value (list of possible texts to apply)
                index = randint(0, len(order_dict[pattern]) - 1)
                print "going to apply index " + str(index)
                output = re.sub(pattern, order_dict[pattern][index], output, 1)
                # then delete that from the list
                del(order_dict[pattern][index])
                print "patterns now look like " + str(order_dict[pattern])
        return output

    def set_regexes(self):
        self.group_name_re = self.group_name_start + r'.+' + self.group_name_end #r'\[#.+#\]'  # surrounded by [# and #]
        self.orderable_re = self.group_pat_start + r'.+' + self.group_pat_end # r'\[\[.+\]\]'  # surrounded by [[ and ]]
        self.group_pattern_re = self.group_name_re + self.orderable_re  # r'\[#.+#\]\[\[.+\]\]'
        self.group_name_cpd_re = self.group_name_start + r'(?P<group_name>.+)' + self.group_name_end #r'\[#.+#\]'
        self.orderable_cpd_re = self.group_pat_start + r'(?P<group_text>.+)' + self.group_pat_end # r'\[\[.+\]\]'  # surrounded by [[ and ]]
        self.group_pattern_cpd_re = self.group_name_cpd_re + self.orderable_cpd_re
