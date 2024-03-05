class Depositor():

    def __init__(self, name, deposit_amount, years):
        self.name = name
        self.deposit_amount = deposit_amount
        self.years = years

    def info(self):
        print('Имя сотрудника:', self.name)
        print('Сумма на счёте:', self.deposit_amount)
        
    def bank(self):
        for i in range(self.years):
            self.deposit_amount = self.deposit_amount + self.deposit_amount * 1/10
        print('Через указанное время на вашем счету будет:' "%.2f" % self.deposit_amount, 'рублей')

input_name = input('Имя сотрудника:')
input_money = int(input('Сколько деняг лежит на счёте:'))
input_years = int(input('На сколько лет:'))
our_depositor = Depositor(input_name, input_money, input_years)

our_depositor.info()
our_depositor.bank()


