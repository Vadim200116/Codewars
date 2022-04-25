
def is_devisable(n,*args):
    return all(not n%a for a in args)
