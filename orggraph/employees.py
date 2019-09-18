from orggraph.dataloader import yaml_loader, file_contents
from orggraph.employee import Employee


class Employees:
    def __init__(self, data_path):
        self.path = data_path
        self.employee_list = self._load_employees()

    def _load_employees(self):
        """Load the supplied employee YAML and convert it into Employee objects."""
        employees = {}

        employees = yaml_loader(file_contents(self.path))["staff"]

        for employee in employees:
            employees[employee] = Employee(employee, employees[employee])

        return employees

    def employees(self):
        return list(self.employee_list.values())
