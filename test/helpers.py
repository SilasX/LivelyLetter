def uniques_after_obj(num, obj, method, *args):
    """get the number of unique results after making num calls to method (as string) of obj
    """
    uniques = set()
    for i in xrange(num):
        uniques.add(getattr(obj, method)(*args))
    return len(uniques)


def uniques_after(num, obj, fctn):
    """get the number of unique results after making num calls of fctn to obj
    """
    uniques = set()
    for i in xrange(num):
        uniques.add(fctn(obj))
    return len(uniques)

