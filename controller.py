from employee_wage import EmployeeWageBuilder
from company import Company


class Operation:

    def __init__(self):
        self.comp_list = []


    def get_comp_details(self, comp_list, name):
        """
        checking the company exist or not
        :param company_list:
        :return:
        """
        # comp_dict = {"name" : comp_list}
        # if comp_dict["name"] == name:
        #     return comp_list, company1

        for company1 in self.comp_list:
            if company1.name == name:
                return comp_list, company1

        comp = Company(name)
        comp_list.append(comp)
        return comp_list, comp


    def get_add_emp(self):
        """
        get employee details

        """
        name = input("Enter company name")  # tcs
        company1_list, company = self.get_comp_details(self.comp_list, name)
        print(company.name)

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

    def show_emp(self):
        """
        get show method
        """
        c_name = input("Enter company name")
        company1_list, company = self.get_comp_details(self.comp_list, c_name)
        print(company.name)
        # comp = Company(c_name)
        company.show_data()

    def get_total_wages(self):
        """
        get total wages
        """

        c_name = input("Enter company name")
        company1_list, company = get_comp_details(self.comp_list, c_name)
        if company.name == c_name:
            print(company.cal_total_wages())


if __name__ == '__main__':
    op = Operation()

    try:
        while True:
            print("""Your choices:- 
                                   1.Add employee
                                   2.Display
                                   3.Total wages"""
                  )
            choice = int(input("Enter your choice:-"))
            menu_dict = {1: op.get_add_emp, 2: op.show_emp, 3: op.get_total_wages}
            menu_dict.get(choice)()
    except Exception:
        print("Please enter numeric value")
