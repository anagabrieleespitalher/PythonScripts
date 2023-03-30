import datetime

#cria a classe empregado com os parametros nome, sobrenome e pagamento
class Employee:


    raise_mount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
    #Classe nome inteiro \Não esquecer o elemento self na instancia
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    #self é a instacia, gera o valor do aumento
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_mount)

     
    #criação de classes, sempre recebe o metodo de classe cls
    @classmethod 
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    #metodo estatico não recebe metodos, não depende de metodos
    #é como uma função
    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
#Subclasses que erdam a employee
class developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

#cargo gerente, herda employee
class manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_em(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


    
#testando o metodo estatico
my_date = datetime.date(2023, 3, 29)
print(Employee.is_working(my_date))

#empregados
dev_1 = developer('Ana','Espitalher', 2500, 'Python')
dev_2 = developer('Henrique', 'Ferreira', 4000, 'Java')
emp_1 = Employee('Rodrigo', 'Alves', 6000)

mgr_1 = manager('Ana', 'Rocha', 10000, [emp_1,dev_2])
print(mgr_1.email)

mgr_1.add_em(dev_1)
mgr_1.remove_emp(emp_1)

print(mgr_1.print_emps())


""" 
print(dev_1.prog_lang)
dev_1.apply_raise()
print(dev_2.prog_lang)
print(dev_1.email)
print(dev_2.email)
print(emp_1.email)

#output empregados
print(Employee.num_of_emps)

 """