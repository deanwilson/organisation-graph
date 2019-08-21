"""Test cases for the Jobs collection object."""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from orggraph.jobs import Jobs  # noqa: E402
from orggraph.job import Job  # noqa: E402


def test_creation():
    """Test basic jobs object creation."""

    jobs = Jobs("data/jobs.yaml")

    # Confirm a known job is present in the loaded objects
    assert "Senior SRE" in jobs.job_list.keys()

    assert isinstance(jobs.job_list["Senior SRE"], Job)
