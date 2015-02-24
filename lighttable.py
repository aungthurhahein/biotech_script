import sys
import texttable
import sh
adict=[['a', 1], ['b', 2], ['c', 3]]

for a, b in enumerate(adict):
    print a,b

def print_all(*args):
    print args[0]
    print args[1]

# yield
def squareCalc(n):
    for i in range(n):
        yield i**2
G= squareCalc(10)
print list(G)
# ascii table
# t = texttable.Texttable((5, 'abc'), (10, 'def'))
# t.row('foobarbaz', 'yadayadayada')
# print t.draw()

sh.ls("-l")