'''
Author: Gray g-ray@qq.com
Date: 2024-04-14 18:34:28
LastEditors: Gray g-ray@qq.com
LastEditTime: 2024-04-14 19:50:29
FilePath: /Package_test/a/module_a.py
Description: 
'''
# a/module_a.py
# import sys
# 相对导入..没有用
from b import module_b

def foo():
    # 使用module_b中的bar函数
    message = module_b.bar()
    return f"> Calling from module_a.foo!\n> {message}"

# 测试导入
if __name__ == "__main__":
    import sys
    print(foo())
