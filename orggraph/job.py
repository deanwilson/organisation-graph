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
            low, high = original_salary.split("-")

            salary["lowest"] = int(low)
            salary["highest"] = int(high)

            salary["median"] = median([salary["lowest"], salary["highest"]])
        else:
            original = int(original_salary)

            salary["lowest"] = original
            salary["highest"] = original
            salary["median"] = original

        return salary
