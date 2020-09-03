"""
处理方法
"""

# 处理打印
def println(str):
    print(str)

# 验证是否非法
def inputConditionValidata(condition, inputTup):
    # 非法判断
    try:
        inputNumT = int(condition)

        # 参数非法 -- 为空
        if inputNumT is None:
            return False

        # 输入参数不包含
        ifExist = inputNumT in inputTup
        if not ifExist:
            return False

        return True
    except BaseException as error:
        return False

# 比较输赢
def compareValidata(cval, pval):
    if (pval == 0 and cval == 2) or (pval == 1 and cval == 0) \
            or (pval == 2 and cval == 1):
        println("---- 电脑赢了！")
    elif pval == cval:
        println("---- 平局！")
    else:
        println("---- 你赢了！")
    println("")