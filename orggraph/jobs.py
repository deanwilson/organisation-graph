from orggraph.job import Job
from orggraph.dataloader import yaml_loader, file_contents


class Jobs:
    def __init__(self, data_path):
        self.path = data_path
        self.job_list = self._load_jobs()

    def _load_jobs(self):
        """Load the supplied job YAML and convert it into Job objects."""
        jobs = {}

        inflated_yaml = yaml_loader(file_contents(self.path))

        jobs = inflated_yaml["jobs"]

        for entry in jobs:
            jobs[entry] = Job(entry, jobs[entry])

        return jobs

    def jobs(self):
        return list(self.job_list.values())
