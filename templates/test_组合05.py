class Mapper:                   #依赖注入
    __mapper_relation = {}

    @staticmethod
    def register(cls,value):
        Mapper.__mapper_relation[cls] = value
    @staticmethod
    def exist(cls):
        if cls in Mapper.__mapper_relation:
            return True
        return False
    @staticmethod
    def value(cls):
        return Mapper.__mapper_relation

class MyType(type):
    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls,*args,**kwargs)
        print('=====在之前输出======')
        arg_list = list(args)
        if Mapper.exist(cls):
            value = Mapper.value(cls)
            arg_list.append(value)
        obj.__init__(*arg_list,**kwargs)
        return obj

class Foo(metaclass=MyType):
    def __init__(self,name):
        print('第二次输出---------')
        self.name = name
    def f1(self):
        print(self.name)

class Bar(metaclass=MyType):
    def __init__(self,name):
        self.name = name
    def f1(self):
        print(self.name)

Mapper.register(Foo,'666')
Mapper.register(Bar,'999')
f = Foo()
print(f.name)
b = Bar()
print(b.name)

#解释器解释流程
#1、遇到class Foo:,执行type的__init__方法
#2，type的init方法做什么？，不知道
# obj = Foo(123)
# print(obj)
# print(obj.name)
#3、执行type的————call方法，执行Foo类的__new__方法，在执行类的__init__方法


