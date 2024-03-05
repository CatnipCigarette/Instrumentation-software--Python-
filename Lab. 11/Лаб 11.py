import datetime

class Worker():
    def __init__(self, surname, salary, date_of_birth):
        self.surname = surname
        self.salary = salary
        self.date_of_birth = date_of_birth

    def age_calculation(self):
        self.date_of_birth = self.date_of_birth.split('-')
        birthday = datetime.date(int(self.date_of_birth[0]),int(self.date_of_birth[1]),int(self.date_of_birth[2]))
        today_date = datetime.date.today()
        age = ((today_date - birthday)/365)
        final_age = str(age)
        print('Возраст работника:', final_age.split()[0])

    def days_to_50(self):
        today = str(datetime.date.today())
        today = today.split('-')
        birthday = input_birth.split('-')
        today_num = datetime.date(int(today[0]),int(today[1]),int(today[2]))
        age = int(today[0]) - int(birthday[0])

        if age < 50:
            up_to_50_left = 50 - age 
            date_50 = datetime.date(int(today[0])+up_to_50_left, int(today[1]), int(today[2]))
            days = date_50 - today_num
            counting = str(days)
            print('Календарных дней до 50 лет:', counting.split()[0])
        else:
            print('Работнику уже исполнилось 50 лет!')
            
input_surname = input('Введите фамилию работника:')
input_money = input('Введите оклад работника в бел. руб:')
input_birth = input('Введите дату рождения сотрудника(гггг-мм-дд):')
our_employee = Worker(input_surname, input_money, input_birth)

print('Фамилия:',our_employee.surname)
our_employee.age_calculation()
our_employee.days_to_50()

