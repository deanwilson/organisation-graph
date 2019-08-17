"""Test cases for the Employee object."""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from orggraph.employee import Employee  # noqa: E402


def test_creation():
    """Test basic employee object creation."""
    name = "Craig Hollis"
    details = {
        "aliases": ["Mr Immortal"],
        "is_a": "Leader",
        "manages": ["DeMarr Davis", "Dinah Soar"],
        "member_of": "Great Lakes Avengers",
        "assigned_to": "Mutant",
    }

    employee = Employee(name, details)

    assert employee.aliases[0] == "Mr Immortal"
