"""Test cases for the Employees collection object."""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from orggraph.employees import Employees  # noqa: E402
from orggraph.employee import Employee  # noqa: E402


def test_creation():
    """Test basic employees object creation."""
    employees = Employees("data/staff-hash.yaml")

    # Confirm a known employee_id is present in the loaded objects
    assert 100018 in employees.employee_list.keys()  # "Tabitha Smith"

    assert isinstance(employees.employee_list[100018], Employee)
