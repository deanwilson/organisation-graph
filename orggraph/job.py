from statistics import median


class Job:
    def __init__(self, title, job_data):
        self.title = title
        self.salary_range = job_data["salary"]
        self.salary = self._extract_salary(job_data["salary"])

    def _extract_salary(self, original_salary):
        salary = {}
        salary["range"] = original_salary

        # if the salary is given as a range extract the upper and lower bounds
        # otherwise use the same value for all 3
        if "-" in original_salary:
            salary["lowest"], salary["highest"] = original_salary.split("-")
            salary["median"] = median([int(salary["lowest"]), int(salary["highest"])])
        else:
            salary["lowest"] = original_salary
            salary["highest"] = original_salary
            salary["median"] = original_salary

        return salary
