from typing import Any


class Dog(object):

    def __init__(self) -> None:
        self.name = "name"

    def __str__(self) -> str:
        print(self.name)
        return super().__str__()


class AnimalFactory(object):
    """单例工厂"""

    # 单例实例对象
    instance = None

    # 记录是否被执行过初始化
    initFlag = False

    def __new__(cls) -> Any:
        """设置new方法"""
        # 如果 instance 不等于空 则不创建新对象
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self) -> None:
        """设置初始化方法 只执行一次"""
        if AnimalFactory.initFlag:
            return

        AnimalFactory.initFlag = True

    def createAnimal(self):
        return Dog()


factory = AnimalFactory()

animal1 = factory.createAnimal()

animal2 = factory.createAnimal()

print(animal1.__str__())
print(animal2.__str__())

# 查看帮助文档
help(AnimalFactory)