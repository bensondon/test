# # def reversed_cmp(x, y):
# #     if x > y:
# #         return -1
# #     if x < y:
# #         return 1
# #     return 0
# print sorted(['ABC','sss','t','hg'],reverse=True)
#
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# f = lazy_sum(1, 3, 5, 7, 9)
# print f()

def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):
             i=j
             return j*j
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1()
print f2()
print f3()

