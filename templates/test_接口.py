#
# #接口类，接口类中的方法不能写任何代码，可以写注释
# class IOrderRepository:
#     def fetch_one_by(self,nid):
#         raise Exception('子类必须实现该方法')
#
# class OrderRepository(IOrderRepository):
#
#     def fetch_one_by(self,nid):
#         print(nid)
#
# obj = OrderRepository()
# obj.fetch_one_by(1)
#
# #普通类
# class Foo:
#     def f1(self):
#         print('123')
#     def f2(self):
#         print('456')
# class bar(Foo):
#     pass
# b = Foo()
# b.f1()

#抽象类
import abc

class Foo:
    def f1(self):
        print('123')

    @abc.abstractmethod
    def f2(self):
        print('456')
class Bar(Foo):
    def f2(self):
        print('aaa')

obj = Bar()
obj.f2()