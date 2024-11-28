class bank(object):
    cash=100000
    @classmethod
    def chk_cash(cls):
        print(cls.cash)
class bob(bank):
    pass
class sbi(bank):
    cash=20000
    def chk_cash(cls):
        print(cls.cash+bank.cash)
b=bob()
b.chk_cash()
b=sbi()
b.chk_cash()