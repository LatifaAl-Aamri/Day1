"""
Exercise Write a Python class Employee with attributes like emp_id , emp_name ,
emp_salary , and emp_department and methods like calculate_emp_salary ,
emp_assign_department , and print employee_details .
Sample Employee Data : " ADAMS " , " E7876 " , 50000 , " ACCOUNTING "
" JONES " , " E7499 " , 45000 , " RESEARCH "
" MARTIN " , " E7900 " , 50000 , " SALES "
" SMITH " , " E7698 " , 55000 , " OPERATIONS "
Use ' assign_department ' method to change the department of an employee .
□ Use ' print employee_details ' method to print the details of an employee .
Use ' calculate_emp_salary ' method takes two arguments : salary and hours_worked , which is
the number of hours worked by the employee . If the number of hours worked is more than 50 ,
the method computes overtime and adds it to the salary . Overtime is calculated as
following formula : overtime = hours worked - 50 Overtime amount = ( overtime * ( salary / 50 ) )
"""

class Employee:
    def __init__(self, empname, empid, empsalary, empdepartment):
        self.empname = empname
        self.empid = empid
        self.empsalary = empsalary
        self.empdepartment = empdepartment
        
    def get_empid(self):
        return self.empid
    
    def get_empname(self):
        return self.empname
    
    def get_empsalary(self):
        return self.empsalary
    
    def get_empdepartment(self):
        return self.empdepartment
    
    # set
    def set_empid(self, newId):
        self.empid = newId
        
    def set_empname(self, newName):
        self.empname = newName
        
    def set_empsalary(self, newSalary):
        self.empsalary = newSalary
        
    def set_empdepartment(self, newDepartment):
        self.empdepartment = newDepartment
    
    def calculate_empsalary(self, hours_worked):
        if hours_worked <= 50:
            return self.empsalary
        else:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.empsalary / 50))
            total_salary = self.empsalary + overtime_amount
            return total_salary
        
    
    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee ID:", self.empid)
        print("Employee Name:", self.empname)
        print("Employee Salary:", self.empsalary)
        print("Employee Department:", self.empdepartment)

 
    def descrip(self):
        return f"Employee name is {self.empname}, id is {self.empid}, salary is {self.empsalary}, department is {self.empdepartment}"

    
    