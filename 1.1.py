#!/usr/bin/python
# -*- coding: UTF-8 -*-
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']
print d.get('test',-1)
print d.pop('Bob')
print d

s = set([1, 1, 2, 2, 3, 3])
print s

s.add(4)
print s

a = ['c', 'b', 'a']
a.sort()
print a

b= 'b'
b.replace('b','B')
print b

print abs(-1)
print "#cmp(x, y)#"
print cmp(1,1)
print cmp(1,2)
print cmp(2,1)

print "#datatype#"
print int('123')
print int(12.34)
print float('12.34')
print str("'aa'")

def age(x):
 if x >= 18:
    pass


def power(x, n):
    s=1
    while n > 0:

        n = n - 1
        s = s * x
    return s

print power(5,2)


def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1,2,a,b,d)