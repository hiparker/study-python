"""读写文件"""
file = None
try:
    # 打开文件 r w a r+ w+ a+
    file = open("README-w.txt", "w")

    # 写文件
    file.write("Hello")

finally:
    # 关闭文件流
    if file is not None:
        file.close()