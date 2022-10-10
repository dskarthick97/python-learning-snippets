""" Module for testing property decorator """

# attribute with property decorator only has read permission
# If write permission is needed, then we have to use setter and getter

# class Animal:

#     def __init__(self) -> None:
#         self._family = "Carnivorous"

#     @property
#     def family(self):
#         return self._family


# animal = Animal()
# animal.family = "Herbivorous"
# print(animal.family)


class Employee:

    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    def full_name(self) -> str:
        return f'{self.first} {self.last}'


emp_1 = Employee("Karthick", "Sabari")

emp_1.first = "Dhilip"

print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name())
