from employee_wage import EmployeeWageBuilder


class Company:

    totalwages_by_company = 0

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
            self.totalwages_by_company = self.totalwages_by_company + employee.compute_wage()
        print(self.totalwages_by_company)
