import random

aList = []
tup = ()

for i in range(0, 100):  # set the range for the list
    aList.append(random.randint(0, 100))  # append a random integer to the list


def TenIsOdd(alist: int):
    """Find the tens digit is odd"""
    for i in alist:
        if i // 10 % 2 != 0:  # Get the tens digit
            print(i, end=' ')


def OneBiggerTen(alist):
    """Find the ones digit is bigger than tens digit"""
    for i in alist:
        if ((i % 10) > (i // 10)) and (i > 10):
            print(i, end=' ')


def FindBetween(alist, n=1, m=100):
    """Find the number between n and m"""
    aList2 = []
    for i in alist:
        if n <= i <= m:  # select the range
            aList2.append(i)  # chose the num which is in the range
            alist.remove(i)
    return aList2, set(alist)  # return a tuple


def OneNotZero(n):
    return n % 10 != 0


if __name__ == '__main__':
    print("Origin list: %s" % aList)
    TenIsOdd(aList)
    # OneBiggerTen(aList)
    #
    # tup = FindBetween(aList, 20, 50)
    # print(tup[0])  # print the result
    # print(tup[1])
    #
    # print(list(filter(OneNotZero, aList)))
    #
    # print(aList)
    #
    # print(list(map(lambda x: x ** 3, aList)))
