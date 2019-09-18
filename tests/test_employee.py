"""Test cases for the Employee object."""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from orggraph.employee import Employee  # noqa: E402


def test_creation():
    """Test basic employee object creation."""

    employee_id = 1001
    details = {
        "name": "Craig Hollis",
        "aliases": ["Mr Immortal"],
        "job_title": "Leader",
        "manages": ["DeMarr Davis", "Dinah Soar"],
        "member_of": "Great Lakes Avengers",
        "teams": ["Mutant"],
    }

    employee = Employee(employee_id, details)

    assert employee.name == "Craig Hollis"
    assert employee.aliases[0] == "Mr Immortal"
