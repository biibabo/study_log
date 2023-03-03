# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 2:48 PM
# @Author  : junbo.zhao
# @File    : test01.py
try:
    a = input('请输入除数:')
    b = input('请输入被除数:')
    c = int(a) / int(b)
    print("您输入的两个数相除的结果是：", c )
except IndexError:
    print("索引错误：运行程序时输入的参数个数不够")
except ValueError:
    print("数值错误：程序只能接收整数参数")
except ArithmeticError:
    print("算术错误")
except Exception:
    print("未知异常")
else:
    print('没有出现异常')