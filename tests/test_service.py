"""Test cases for the Service object."""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from orggraph.service import Service  # noqa: E402


def test_creation():
    """Test basic service object creation."""
    name = "OrderDB"
    details = {
        "owner": "The brave few",
        "technologies": [
            "Linux",
            "Java",
            "MySQL",
        ]
    }

    service = Service(name, details)

    assert service.owner == "The brave few"
    assert "Java" in service.technologies
