#组合降低代码与代码间的依赖
class SqlHelper:
    def fetch_one(self):
        pass
    def fetch_all(self):
        pass

class UserInfo:
    def __init__(self,helper):
        self.s = helper
    def login(self):
        self.s.fetch_one()
    def user_list(self):
        self.s.fetch_all()

h = SqlHelper()
obj = UserInfo(h)
obj.login()
