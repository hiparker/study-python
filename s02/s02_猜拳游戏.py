# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import s02.method.handler as Handler
import random


# 定义参数
#   循环条件
flag = True
#   输入参数（用于非法判断）
inputTup = (0, 1, 2, 3)
Handler.println("猜拳游戏 xxxxxxx")
Handler.println("")


while flag:
    inputNum = None
    inputStr = input("请出拳 0--石头 | 1--剪刀 | 2--布 | 3--结束：")

    # 处理条件
    valiFlag = Handler.inputConditionValidata(inputStr, inputTup)

    if not valiFlag:
        Handler.println("参数非法")
        Handler.println("")
        continue

    # 获得系统出拳
    computer = random.randint(0, 2)

    inputNum = int(inputStr)

    # 退出
    if 3 == inputNum:
        flag = False
        Handler.println("游戏结束")
        Handler.println("")
        break

    # 比较输赢
    Handler.compareValidata(computer, inputNum)
