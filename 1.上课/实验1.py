import random


aList = []

for i in range(0, 100):  # set the range for the list
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

tup = ()


def FindBetween(alist, n=1, m=100):
    aList2 = []
    for i in alist:
        if n <= i <= m:
            aList2.append(i)
            alist.remove(i)
    return (aList2, set(alist))


tup = FindBetween(aList, 20, 50)
print(tup[0])
print(tup[1])

# def OneNotZero(n):
#     return n % 10 != 0


# print(list(filter(OneNotZero, aList)))


# print(aList)
# print(list(map(lambda x: x ** 3, aList)))
