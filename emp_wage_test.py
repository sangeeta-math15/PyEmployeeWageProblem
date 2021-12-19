from emp_wage_builder import EmpWageBuilder
import pytest

emp = EmpWageBuilder()
def test_check_attendance():
    assert (emp.emp_attendence() == 8 or emp.emp_attendence() == 4 or emp.emp_attendence() == 0)

def test_daily_wage():
    assert emp.cal_daily_wage(8) == 160
    assert emp.cal_daily_wage(4) == 80
    assert emp.cal_daily_wage(0) == 0

