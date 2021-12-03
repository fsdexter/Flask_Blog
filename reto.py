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


    def __str__(self):
        return f'El empleado {self.name} {self.surname} cobra {self.pay}'


    def __add__(self, other):
        return self.pay + other.pay


    def pay_rise(self):
        self.pay = int(self.pay * 1.15)


    @classmethod
    def from_string(cls,string):
        name, surname = string.split(',')
        return cls(name, surname)





'''
**Sergio Pesquera**, 
**Miguel Betegon**
**Enrique Pernia**
'''

#emp_x = Empleado('name', 'surname')

emp_1 = Empleado('Sergio', 'Pesquera')
emp_2 = Empleado('Miguel', 'Betegon')
emp_3 = Empleado('Enrique', 'Pernia')
Jaled = Empleado.from_string("Jaled, Moustafa")

print(emp_1)
print(emp_2)
print(emp_3)
print(Jaled)


# print(emp_1.name, emp_1.surname,emp_1.email,emp_1.pay, emp_1.id)
# print(emp_2.name, emp_2.surname,emp_2.email,emp_2.pay, emp_2.id)
# print(emp_3.name, emp_3.surname,emp_3.email,emp_3.pay, emp_3.id)
# print(Jaled.name, Jaled.surname,Jaled.email,Jaled.pay, Jaled.id)
# emp_1.pay_rise()
# print(emp_1.pay)
# emp_2.pay_rise()
# print(emp_2.pay)
# emp_3.pay_rise()
# print(emp_3.pay)


# jaled=Empleado("Jaled, Moustafa, 1600")


class CEO(Empleado):

    def __init__(self, name, surname, employee=None ):
        super().__init__(name, surname)
        if employee is None:
            self.employee = []
        else:
            self.employee = employee

    
    def add_employee(self, employee):
        if employee not in self.employee:
            self.employee.append(employee)
    
    
    def remove_employee(self, employee):
        if employee in self.employee:
            self.employee.remove(employee)