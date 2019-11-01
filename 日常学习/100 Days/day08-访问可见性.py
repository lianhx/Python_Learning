class Test:

    def __init__(self, foo):
        self.__foo = foo  # 私有属性以两个下划线为开头

    def __bar(self):
        print(self.__foo)
        print('__bar')

# def main():     # 报错
#     test = Test('hello')
#     test.__bar()
#     print(test.__foo)

def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)

if __name__ == "__main__":
    main()
