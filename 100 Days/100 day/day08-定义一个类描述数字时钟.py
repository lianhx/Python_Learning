import time


class Clock(object):
    # 数字时钟
    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour  # 以单下划线开头来表示属性是受保护的
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % \
                (self._hour, self._minute, self._second)

def main():
    clock = Clock(23, 59, 55)
    while True:   # ctrl+c 停止程序
        print(clock.show())
        time.sleep(1)
        clock.run()

if __name__ == '__main__':
    main()
