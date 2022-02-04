import random


class EmployeeWageBuilder:
    is_present = 1
    is_part_time = 2
    full_day_hr = 8
    part_time_hr = 4

    def __init__(self, employee_dict):
        """
        :param name: string name of the company
        :param maximum_working_days: int
                        maximum working days a employee has to work in a month
        :param maximum_working_hours: int
                        maximum working hours a employee has to work in a month
        :param wage_per_hour:  amount getting paid per hour for employee

        """

        self.name = employee_dict.get("name")
        self.maximum_working_days = employee_dict.get("maximum_working_days")
        self.maximum_working_hours = employee_dict.get("maximum_working_hours")
        self.wage_per_hour = employee_dict.get("wage_per_hour")

    def employee_check(self, value):
        """
        :param value:  random number between 0 to 2 .
                if the number is 1, employee present; 2: part time 0;absent
        :return: employee working hours based on random number
        """
        switcher = {
            self.is_present: self.full_day_hr,
            self.is_part_time: self.part_time_hr,
        }
        return switcher.get(value, 0)

    def compute_wage(self):
        """
        calculates daily wage and total wage of the employee
        :parameter : parameters are taken from constructor
        prints the total wage of the respective company's employee
        :return:
        """
        global daily_wage
        working_days = 0
        working_hours = 0
        self.daily_wage = 0
        self.employee_working_hours = 0
        while working_days < self.maximum_working_days and working_hours < self.maximum_working_hours:  # Calculating wages for month
            random_number = random.randrange(0, 3)  # To obtain a random number between 0 and 3
            employee_working_hours = self.employee_check(random_number)
            daily_wage = self.wage_per_hour * employee_working_hours
            working_days += 1
            working_hours += employee_working_hours
        return daily_wage
