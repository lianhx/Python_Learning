import os
import time


def main():
    content = '北京欢迎你，为你开天辟地.........'
    while True:
        os.system('cls')  # 清理屏幕上的输出  os.system('clear')
        print(content)
        time.sleep(0.2)  # 200ms
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
