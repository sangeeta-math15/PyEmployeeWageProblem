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
        total_wage = 0
        self.daily_wage = 0
        self.employee_working_hours = 0
        while working_days < self.maximum_working_days and working_hours < self.maximum_working_hours:  # Calculating wages for month
            random_number = random.randrange(0, 3)  # To obtain a random number between 0 and 3
            employee_working_hours = self.employee_check(random_number)
            daily_wage = self.wage_per_hour * employee_working_hours
            working_days += 1
            working_hours += employee_working_hours
            total_wage = total_wage + daily_wage
        return total_wage


class Company:
    totalwages_by_company1 = 0

    def __init__(self, name):
        """
        :param name:
        """
        self.name = name
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)
        print(employee.compute_wage())

    def show_data(self):
        """

        :return: show data method returns data
        """
        print("Company name is :- ", company.name)
        for employee1 in self.employee_list:
            print("employee name: ", employee1.name)
            print("maximum working hour of company:", employee1.maximum_working_days)
            print("maximum working hour of company:", employee1.maximum_working_hours)
            print("Employee working hour: ", employee1.wage_per_hour)

    def cal_total_wages(self):
        """
        calling calculate wages in company class
        :return:
        """
        for employee in self.employee_list:
            self.totalwages_by_company1 = self.totalwages_by_company1 + employee.compute_wage()
        print(self.totalwages_by_company1)


def get_comp_details( comp_list, name ):
    """
    checking the company exist or not
    :param company_list:
    :return:
    """
    for company1 in comp_list:
        if company1.name == name:
            return comp_list, company1

    comp = Company(name)
    comp_list.append(comp)
    return comp_list, comp


if __name__ == '__main__':
    comp_list = []
    while True:
        print("Enter your choice")
        print("1 Add Employee")
        print("2 Show details")
        print("3 total wages ")
        choice = int(input("Enter your choice"))
        if choice == 1:
            name = input("Enter company name")  # tcs
            company1_list, company = get_comp_details(comp_list, name)
            print(company1_list, company.name)
            name = input("Enter emp name:- ")
            maximum_working_days = int(input("Enter emp max working day:- "))
            maximum_working_hours = int(input("Enter the emp company working hour:- "))
            wage_per_hour = int(input("Enter the employee wages per hour in company"))
            employee_dict = {
                "name": name, "maximum_working_days": maximum_working_days,
                "maximum_working_hours": maximum_working_hours, "wage_per_hour": wage_per_hour
            }
            employee = EmployeeWageBuilder(employee_dict)
            company.add_employee(employee)

        elif choice == 2:
            c_name = input("Enter company name")
            company1_list, company = get_comp_details(comp_list, c_name)
            company.show_data()
        elif choice == 3:
            c_name = input("Enter company name")
            company1_list, company = get_comp_details(comp_list, c_name)
            print(company.cal_total_wages())
        else:
            break
