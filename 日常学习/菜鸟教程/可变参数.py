def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


nums = [1, 2]
print(calc(1, 2))
print(calc(*nums))
print(calc())
