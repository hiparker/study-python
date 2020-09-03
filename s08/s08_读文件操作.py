"""读文件"""
file = None
try:
    # 打开文件
    file = open("README-r.txt")

    # 读文件
    # for i in file.read():
    hasNext = True
    while hasNext:
        readTemp = file.readline()
        # 如果没有下一行 文件流结束
        if not readTemp:
            hasNext = False
            break

        # 打印行
        print(readTemp)

finally:
    # 关闭文件流
    if file is not None:
        file.close()
