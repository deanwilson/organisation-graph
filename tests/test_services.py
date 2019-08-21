"""Test cases for the Services collection object."""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from orggraph.services import Services  # noqa: E402
from orggraph.service import Service  # noqa: E402


def test_creation():
    """Test basic Services object creation."""

    services = Services("data/services.yaml")

    # Confirm a known service is present in the loaded objects
    assert "Inventory Tracker" in services.service_list.keys()

    assert isinstance(services.service_list["Inventory Tracker"], Service)
