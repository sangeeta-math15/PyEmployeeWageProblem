import logging
import random


logging.basicConfig(filename='emp_wage.log', filemode='w')
log = logging.getLogger()
log.setLevel(logging.DEBUG)


class EmpWageBuilder:

    def __init__(self):
        self.check_attendence=0

    def emp_attendence(self):
        is_full_time = 1
        check_attendence = random.randint(0, 1)
        if check_attendence == is_full_time:
            log.info("Employee is present")
            emp_hr = 8
            return emp_hr
        else:
            log.info("Employee is absent")
            emp_hr = 0
            return emp_hr

    # Create employeeWageBuilder class
    def cal_daily_wage(self, emp_hr):
        emp_wage_per_hour = 20
        emp_wage = emp_hr * emp_wage_per_hour
        return emp_wage


if __name__ == '__main__':
    emp = EmpWageBuilder()
    emp_hr = emp.emp_attendence()
    daily_wage = emp.cal_daily_wage(emp_hr)
    print(daily_wage)
