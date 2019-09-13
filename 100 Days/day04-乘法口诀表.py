for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')  # \t为横向制表符
    print()  # 本身自带换行，如果是print('\n')相当于换行两次
