class Dog:

    def __init__(self,name):
        self.name = name

    def eat(self):
        print(self.name+" 吃狗粮")

    def run(self):
        print(self.name+" 四条腿摇尾巴跑")

dog1 = Dog("旺财")
dog2 = Dog("黑虎")

dog1.eat()
dog1.run()

dog2.eat()
dog2.run()