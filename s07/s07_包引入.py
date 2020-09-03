
import time
import s07.tools as tools

# 获得当前时间
date = tools.DateTool.getDate()
# 打印原始时间
tools.PrintTool.printDate(date)
# 打印格式化后时间
tools.PrintTool.printStr(time.strftime("%Y-%m-%d %H:%M:%S", date))