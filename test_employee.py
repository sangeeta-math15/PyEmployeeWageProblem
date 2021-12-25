from employee_wage import EmployeeWageBuilder
from employee_wage import Company

import pytest

def test_compute_wage():
    """
    testing the compute wage
    :return:
    """
    emp1 = EmployeeWageBuilder("sangeeta", 20, 100, 20)
    # assert (emp1.compute_wage() == 2 or emp1.compute_wage() == 1 or emp1.compute_wage() == 0)
    assert isinstance(emp1.compute_wage() , int) == True

def test_emp_check():
    """
    :return:
    """
    emp1 = EmployeeWageBuilder("sangeeta", 20, 100, 20)
    assert (emp1.employee_check(2) == 8 or emp1.employee_check(1) == 4 or emp1.employee_check(0) == 0)

def test_add_employee():
    """
    :return:
    """
    c = Company("zensar")
    emp1 = EmployeeWageBuilder("sangeeta", 20, 100, 20)
    c.add_employee(emp1)
    assert not len(c.employee_list) <= 0
    assert isinstance(c.employee_list, list)


def test_get_comp_details():
    """
    :return:
    """
    comp = Company("wipro")
    assert isinstance(comp, Company) == True
