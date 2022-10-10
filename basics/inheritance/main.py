
import employee
import payroll_interface

salary_employee = employee.SalaryEmployee(18, 'Virat Kohli', 18000)
hourly_employee = employee.HourlyEmployee(23, 'Karthick Sabari', 8, 50)
commission_employee = employee.CommissionEmployee(7, 'Bruce Wayne', 15000, 3700)

payrolls = payroll_interface.IPayroll()
payrolls.calculate_payroll([salary_employee, hourly_employee, commission_employee])

"""
Case 1: Can able to call directly the calculate_payroll method with its 
        respective instance.

Case 2: Can able to make the Employee class as abstract class and mark the 
        calculate_payroll method as abstract_method. So in a way, forcing the 
        derived classes to implement the method.

Implementation inheritance vs interface inheritance
"""
