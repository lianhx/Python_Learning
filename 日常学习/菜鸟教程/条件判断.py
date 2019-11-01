# age = 3
# if age >= 18:
#     print('your age is', age)
#     print('adult')
# elif age >= 6:
#     print('teenger')
# else:
#     print('your age is', age)
#     print('kid')
s = input('birth:')  # input返回的是str
birth = int(s)  # 转换成整数
if(birth < 2000):
    print('before 00')
else:
    print('after 00')
