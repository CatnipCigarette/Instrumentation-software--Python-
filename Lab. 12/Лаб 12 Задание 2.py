from random import randint

class Bank_account():

    defolt_type = 'Личный'
    
    def __init__(self, аccount_number, balance):
        self.аccount_number = аccount_number
        self.balance = balance

    def account_info(self):
        self.аccount_number = number
        self.balance = money
        print('Номер счёта:', self.аccount_number)
        print('Баланс:', self.balance)
        print('Тип аккаунта:', self.defolt_type)

    def cash_withdrawal():
        withdrawal_amount = int(input('Введите сумму снятия:'))
        balance = money
        if balance < withdrawal_amount:
            print('Недостаточно средств!')
        else:
            balance -= withdrawal_amount
            print('Операция завершена успешно!')
            print('Остаток на счёте:', balance)

    def refill():
        replenishment_amount = int(input('Введите сумму пополнения:'))
        balance = money
        balance += replenishment_amount
        print('Операция завершена успешно!')
        print('Остаток на счёте:', balance)

name = input('Введите своё имя:')
print('Добрый день,', name,', приветствуем вас в эл. кабинет!')
            
number = randint(100000, 199999)
money = randint(1, 15000)

my_account = Bank_account(number, money)
my_account.account_info()

flag = True
while flag:  
    print('Хотите ли провести ещё какую-либо операцию?')
    action = int(input('1 - снять деньги, 2 - положить деньги, 3 - завершить сеанс '))
    if action == 1:
        Bank_account.cash_withdrawal()
    elif action == 2:
        Bank_account.refill()
    elif action == 3:
        print('Сеанс завершён, всего доброго,', name, '!')
        flag = False
    else:
        print('\n', 'Такого действия не существует, попробуйте ещё раз!', '\n')


    


