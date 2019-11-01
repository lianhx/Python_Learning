L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])  # 取前三个元素
print(L[:3])  # 取前三个元素，如果第一个索引为0，可省略
print(L[-2:])  # 取倒数两个元素
print(L[-2:-1])  # 倒数第一个索引为-1

N = list(range(100))  # 创建一个0-99的序列
print(N[-10:])  # 取最后10个元素
print(N[10:20])  # 取11-20个数
print(N[:10:2])  # 前10个数，每两个取一个
print(N[::5])  # 所有数每5个取一个
