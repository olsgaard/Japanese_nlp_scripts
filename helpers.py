# Flatten function from official compiler python module (decapriated in python 3.x)
# https://hg.python.org/cpython/file/3e7f88550788/Lib/compiler/ast.py#l7
#
# used to flatten a list or tupel
#
# [1,2[3,4],[5,[6,7]]] -> [1,2,3,4,5,6,7]


def flatten(seq):

    l = []

    for elt in seq:

        t = type(elt)

        if t is tuple or t is list:

            for elt2 in flatten(elt):

                l.append(elt2)

        else:

            l.append(elt)

    return l