from yaml import load, SafeLoader
from orggraph.job import Job


class Jobs:
    def __init__(self, data_path):
        self.path = data_path
        self.job_list = self._load_jobs()

    def _load_jobs(self):
        """Load the supplied job YAML and convert it into Job objects."""
        jobs = {}
        yaml = None

        with open(self.path, "r") as yaml_file:
            yaml = yaml_file.read()

        inflated_yaml = load(yaml, Loader=SafeLoader)
        jobs = inflated_yaml["jobs"]

        for entry in jobs:
            jobs[entry] = Job(entry, jobs[entry])

        return jobs

    def jobs(self):
        return list(self.job_list.values())
