from emp_wage_builder import EmpWageBuilder
import pytest
def test_check_attendance():
    emp = EmpWageBuilder()
    assert emp.emp_attendence() == "Employee is present"


