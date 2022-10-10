
class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):

    def __init__(self, id, name, pay_per_month):
        super().__init__(id, name)
        self.pay_per_month = pay_per_month

    def calculate_payroll(self):
        return self.pay_per_month


class HourlyEmployee(Employee):

    def __init__(self, id, name, hours_worked, pay_per_hour):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.pay_per_hour = pay_per_hour

    def calculate_payroll(self):
        return self.hours_worked * self.pay_per_hour


class CommissionEmployee(SalaryEmployee):

    def __init__(self, id, name, pay_per_month, commission):
        super().__init__(id, name, pay_per_month)
        self.commission = commission

    def calculate_payroll(self):
        pay_per_month = super().calculate_payroll()
        return pay_per_month + self.commission
