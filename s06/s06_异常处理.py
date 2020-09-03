# 捕获机制
try:
    a = 1 / 0
except:
    print('计算异常')

# 除0 异常
try:
    a = 1 / 0
except ZeroDivisionError:
    print("除0异常")

# 未知异常
try:
    a = 1 / "阿"
except ZeroDivisionError:
    print("除0异常")
except Exception as e:
    print("未知异常"+e.__str__())


# 主动抛出异常
try:
    raise Exception("主动抛出异常")
    a = 1 / 0
except ZeroDivisionError:
    print("除0异常")
except Exception as e:
    print("未知异常" + e.__str__())
finally:
    print("执行完毕")

# finally
try:
    a = 1 / 0
except ZeroDivisionError:
    print("除0异常")
except Exception as e:
    print("未知异常" + e.__str__())
finally:
    print("执行完毕")