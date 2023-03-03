# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 2:30 PM
# @Author  : junbo.zhao
# @File    : try-except.py

try:
    fh = open("testfile", "a")
    fh.writelines("123")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

