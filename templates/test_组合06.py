
     #依赖注入
class Mapper:
    # 在字典里定义依赖注入关系
    __mapper_relation = {}

    # 类直接调用注册关系
    @staticmethod
    def register(cls, value):
        Mapper.__mapper_relation[cls] = value

    @staticmethod
    def exist(cls):
        if cls in Mapper.__mapper_relation:
            return True
        return False

    @staticmethod
    def get_value(cls):
        return Mapper.__mapper_relation[cls]

class MyType(type):
    def __call__(cls, *args, **kwargs):
        obj = cls.__new__(cls, *args, **kwargs)
        arg_list = list(args)
        if Mapper.exist(cls):
            value = Mapper.get_value(cls)
            arg_list.append(value)
        obj.__init__(*arg_list, **kwargs)
        return obj

class Head:
    def __init__(self):
        self.name = 'alex'

class Foo(metaclass=MyType):
    def __init__(self, h):
        self.h = h

    def f1(self):
        print(self.h)


class Bar(metaclass=MyType):
    def __init__(self, f):
        self.f = f

    def f2(self):
        print(self.f)


Mapper.register(Foo, Head())
Mapper.register(Bar, Foo())

b = Bar()
print(b.f.h)