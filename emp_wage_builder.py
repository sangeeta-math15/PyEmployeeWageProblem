import logging
import random

logging.basicConfig(filename='emp_wage.log',filemode='w')
log=logging.getLogger()
log.setLevel(logging.DEBUG)

#Create employeeWageBuilder class
class EmpWageBuilder:
    def __init__(self):
        self.check_attendence=0
    def emp_attendence(self):
        check_attendence=random.randint(0,1)
        if check_attendence == 0:
            log.info("Employee is present")
            return "Employee is present"
        else:
            return "Employee is absent"

if __name__ == '__main__':
    emp=EmpWageBuilder()
    print(emp.emp_attendence())




