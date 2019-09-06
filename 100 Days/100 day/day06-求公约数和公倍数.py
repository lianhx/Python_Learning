# 求最大公约数greatest common divisor
def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

# 求最小公倍数Least Common Multiple
def lcm(x, y):
    return x * y // gcd(x, y)
