
class IPayroll:

    def calculate_payroll(self, employees):
        for employee in employees:
            print('Payroll for {} - {}'.format(employee.id, employee.name))
            payroll = employee.calculate_payroll()
            print('Calculated payroll is {}'.format(payroll))
            print('')
