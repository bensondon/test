#!/usr/bin/python
# -*- coding: UTF-8 -*-
classmate=['a','b','c','d']
print classmate
len_count=len(classmate)
print len_count
class_cnt=classmate[-1]
print class_cnt
class_append=classmate.append('e')
print classmate
class_insert=classmate.insert(0,'abc')
print classmate
classmate.pop(1)
print classmate
classmate.pop()
print classmate
sum=0
classmate=range(101)
for aa in classmate:
      sum=sum+aa
      print sum


sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print sum
print n
