# python 的package以及目录组织相关问题

```
├── a
│   ├── __init__.py
│   ├── module_a.py
├── b
│   ├── __init__.py
│   ├── module_b.py
├── __init__.py
├── README.md
└── test.py

```



在这个例子里面，a，b 互相不可见。直接运行module_a不能使用module_b的函数，即使使用了相对导入也没有用

我认为这是合理的，package 直接确实不能直接互相调用，毕竟我们不会直接运行module_a，这样不合理，更合理的方案是在project层面使用两个package，代码不用修改，因为站在test的角度，可以看见两个package，此时通过调用module_a简洁调用module_b的行为是被支持的，我猜测原因可能是python作为脚本语言特性，相当于换一个位置加载脚本，所以能正确运行

## 参考

1. [【python】引用各种路径下的package和module](https://blog.csdn.net/AXIMI/article/details/100552142)
2. 