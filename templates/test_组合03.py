class Foo:
    def __init__(self,name):
        self.name = name
    def f1(self):
        print(self.name)

#解释器解释流程
#1、遇到class Foo:,执行type的__init__方法
#2，type的init方法做什么？，不知道
obj = Foo(123)
print(obj.name)
#3、执行type的————call方法，执行Foo类的__new__方法，在执行类的__init__方法


