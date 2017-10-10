# -*- coding: UTF-8 -*-
# map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
# def f(x):
#     return x * x
# print map(f,[1,2,3,4,5,6,7,8])

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# def fn(x, y):
#     return x * 10 + y
# print reduce(fn, [1, 3, 5, 7, 9])

# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#     return reduce(fn, map(char2num, s))
# print str2int('0222')

# def char2num(s):
#      return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# print map(char2num,'123')
# def prod(x,y):
#      return  x * y
# print reduce(prod,[1,2,3,4,5,6,7])

# def cg_str(lst):
#     return list(map(lambda x:x[0].lower()+x[1:].lower(),lst))
# print (cg_str(['adam','LISA','barT']))

def f(s):
    return s.title()
print map(f,['adam', 'LISA', 'barT'])