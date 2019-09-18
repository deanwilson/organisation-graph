"""Test the Job object and its properties."""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from orggraph.job import Job  # noqa: E402

# TODO: Test all values on a range of 1


def test_salary():
    """Ensure the Job object has a salary defined."""
    title = "Test Writer"
    job_details = {"salary": "123456"}

    job = Job(title, job_details)

    assert job.salary_range == "123456"


def test_salary_range():
    """Ensure the salary range parsing code is working correctly."""
    title = "Test Writer"
    job_details = {"salary": "12345-54321"}

    job = Job(title, job_details)

    assert job.salary["lowest"] == 12345
    assert job.salary["highest"] == 54321
