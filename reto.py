import random


class Empleado:

    available_id = 1 

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.email = name + '.' + surname + '@email.com'
        self.pay = random.randint(1500, 2200)
        self.id = Empleado.available_id

        Empleado.available_id += 1

    def pay_rise(self):
        self.pay = int(self.pay * 1.15)




'''
**Sergio Pesquera**, 
**Miguel Betegon**
**Enrique Pernia**
'''

#emp_x = Empleado('name', 'surname')

emp_1 = Empleado('Sergio', 'Pesquera')
emp_2 = Empleado('Miguel', 'Betegon')
emp_3 = Empleado('Enrique', 'Pernia')


print(emp_1.name, emp_1.surname,emp_1.email,emp_1.pay)
print(emp_2.name, emp_2.surname,emp_2.email,emp_2.pay)
print(emp_3.name, emp_3.surname,emp_3.email,emp_3.pay)

emp_1.pay_rise()
print(emp_1.pay)
emp_2.pay_rise()
print(emp_2.pay)
emp_3.pay_rise()
print(emp_3.pay)


