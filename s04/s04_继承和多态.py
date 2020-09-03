class Animal(object):
    """
        动物抽象类 具体方法不执行
        包含 eat run 两个方法
    """

    def eat(self):
        pass

    def run(self):
        pass


class Dog(Animal):
    """狗类"""

    def run(self):
        print("四条腿 摇着尾巴跑")

    def eat(self):
        print("吃狗粮")


class Cat(Animal):
    """猫类"""

    def eat(self):
        print("四条腿 夹着尾巴跑")

    def run(self):
        print("吃猫粮")


animal = Cat()
# animal = Dog()
animal.run()
animal.eat()
