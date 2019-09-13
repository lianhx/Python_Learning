def main():
    str1 = 'hello, world!'
    print(len(str1))  # 计算字符串长度
    print(str1.capitalize())  # 获得字符串首字母大写的拷贝 'Hello,world!'
    print(str1.upper())  # 字符串大写的拷贝 'HELLO,WORLD!'
    print(str1.find('or'))  # 从字符串中查找子串所在位置  8
    print(str1.find('shit'))  # -1
    #print(str1.index('or'))  # 跟find类似，但找不到子串时会引发异常
    #print(str1.index('shit'))
    print(str1.startswith('He'))  # 检查字符串是否以指定的字符串开头 False
    print(str1.startswith('hel'))  # True
    print(str1.endswith('!'))  # 检查字符串是否以指定的字符串结尾  True
    print(str1.center(50, '*'))  # 将字符串在指定的宽度居中并在两侧填充指定的字符
    print(str1.rjust(50, ' '))  # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    str2 = 'abc123456'
    print(str2[2])  # c 从字符串中取出指定位置的字符(下标运算)
    print(str2[2:5])  # 字符串切片  c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45
    print(str2.isdigit())  # 检查字符串是否由数字构成 False
    print(str2.isalpha())  # 检查字符串是否由字母构成 False
    print(str2.isalnum())  # 检查字符串是否由数字和字母构成 True
    str3 = '  lianhaixu88@163.com  '
    print(str3)
    print(str3.strip())  # 获得字符串修剪左右两边空格的拷贝



if __name__ == '__main__':
    main()
