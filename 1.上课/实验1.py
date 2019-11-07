import random

aList = []
for i in range(0, 100):
    aList.append(random.randint(0, 100))
# print(aList)


# def TenIsOdd(alist: int):
#     '''Find the tens digit is odd'''
#     for i in alist:
#         if i // 10 % 2 != 0:  # Get the tens digit
#             print(i, end=' ')


# TenIsOdd(aList)


# def OneBiggerTen(alist):
#     '''Find the ones digit is bigger than tens digit'''
#     for i in alist:
#         if ((i % 10) > (i // 10)) and (i > 10):
#             print(i, end=' ')


# OneBiggerTen(aList)


# def FindBetween(alist, n=1, m=100):
#     for i in alist:
#         if n < i < m:

def OneNotZero(n):
    return n % 10 != 0


newlist = list(filter(OneNotZero, aList))
print(newlist)
