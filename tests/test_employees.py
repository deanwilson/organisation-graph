"""Test cases for the Employees collection object."""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from orggraph.employees import Employees  # noqa: E402
from orggraph.employee import Employee  # noqa: E402


def test_creation():
    """Test basic employees object creation."""

    employees = Employees("data/staff.yaml")

    # Confirm a known employee is present in the loaded objects
    assert "Tabitha Smith" in employees.employee_list.keys()

    assert isinstance(employees.employee_list["Tabitha Smith"], Employee)
