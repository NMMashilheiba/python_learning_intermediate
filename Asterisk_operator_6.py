# custom object copying
import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Anna', 23)
p2 = Person('Meena', 24)

company = Company(p1, p2)
#company_clone = copy.copy(company)             #shallow copy
company_clone = copy.deepcopy(company)          #deepcopy
company_clone.boss.age = 40

print(company.boss.age, 'original')
print(company_clone.boss.age, 'copy')

# p2.age = 21
# print(p1.age)
# print(p2.age)
