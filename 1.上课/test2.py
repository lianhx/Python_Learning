class Device():
    def __init__(self, name=' ', weight=0):
        # init object name and weight
        self.name = name
        self.weight = weight

    def setName(self, name):
        self.name = name

    def setWeight(self, weight):
        self.weight = weight

    def setNameAndWeight(self, name, weight):
        self.name = name
        self.weight = weight


class Motor(Device):
    def __init__(self, name=' ', weight=0, gas=0):
        self.name = name
        self.weight = weight
        self.gas = gas

    def printDetails(self):
        print('name:%s, weight:%f, gas:%s' % (self.name, self.weight, self.gas))


if __name__ == '__main__':
    dev1 = Device()
    dev2 = Device()
    dev1.setNameAndWeight('Screen', 20)
    dev2.setNameAndWeight('Camera', 9)
    print('dev1: name:%s, weight:%f' % (dev1.name, dev1.weight))
    print('dev2: name:%s, weight:%f' % (dev2.name, dev2.weight))

    mot1 = Motor()
    mot1.setName('Stepping')
    mot1.printDetails()
