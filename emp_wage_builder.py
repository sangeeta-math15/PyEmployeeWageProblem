import logging
import random

logging.basicConfig(filename='emp_wage.log', filemode='w')
log = logging.getLogger()
log.setLevel(logging.DEBUG)


class EmpWageBuilder:

    def __init__(self, emp_hr=0, emp_wage=0, total_emp_wage=0, total_working_days=0, total_working_hours=0):
        self.emp_hr = emp_hr
        self.emp_wage = emp_wage
        self.total_emp_wage = total_emp_wage
        self.total_working_days = total_working_days
        self.total_working_hours = total_working_hours

    def total_employee_wage(self):
        no_working_day = 20
        emp_rate_per_hr = 20
        max_hrs_in_month = 100
        while self.total_working_hours <= max_hrs_in_month and self.total_working_days <= no_working_day:
            self.total_working_days += 1
            emp_check = random.randint(1, 3)
            self.emp_hr = self.get_work_hours(emp_check)
            self.total_working_hours = self.total_working_hours + self.emp_hr
            print("totalworking hour", self.total_working_hours)
            print("Days: {} Emp Hr: {}".format(self.total_working_days, self.emp_hr))
            self.emp_wage = self.emp_hr * emp_rate_per_hr
            self.total_emp_wage = self.total_emp_wage + self.emp_wage
            print("Total conditional wage:", self.total_emp_wage)

    def get_work_hours(self, value):
        switcher = {
            1: 8, 2: 4, 3: 0
        }
        return switcher.get(value)


if __name__ == '__main__':
    emp = EmpWageBuilder()
    emp.total_employee_wage()
