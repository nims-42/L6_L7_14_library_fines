import pytest
from library_fines import late_fine, can_borrow, renewal_status

#Example test cases:
def test_returned_on_time():
    assert late_fine("student", 10, False) == 0

def test_can_borrow():
    assert can_borrow(1, 0, "student") is True

#Write the rest of the test cases so that the code is 90- 100% covered.

# Code (line) coverage tests
def test_unknown_member():
    with pytest.raises(ValueError):
        late_fine("alien", 5, False)

def test_negative_days():
    with pytest.raises(ValueError):
        late_fine("student", -1, False)

def test_faculty_overdue():
    assert late_fine("faculty", 35, False) == 5

def test_student_fine_capped():
    assert late_fine("student", 200, False) == 200

def test_damaged_book():
    assert late_fine("student", 10, True) == 150

def test_borrow_blocked_by_fine():
    assert can_borrow(0, 150, "student") is False

def test_faculty_can_borrow():
    assert can_borrow(5, 0, "faculty") is True

def test_renewal_denied():
    assert renewal_status(0, True, 5) == "denied"

def test_renewal_limit_reached():
    assert renewal_status(2, False, 5) == "limit reached"

def test_renewal_overdue():
    assert renewal_status(0, False, -1) == "overdue"

def test_renewal_ok():
    assert renewal_status(0, False, 5) == "renewed"

