# 函数
def fib(n):
    """斐波那契数列"""
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a + b
    print()
