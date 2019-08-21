from orggraph.dataloader import yaml_loader, file_contents
from orggraph.service import Service


class Services:
    def __init__(self, data_path):
        self.path = data_path
        self.service_list = self._load()


    def _load(self):
        """Load the supplied service YAML and convert it into Service objects."""
        services = {}

        services = yaml_loader(file_contents(self.path))["services"]

        for service in services:
            services[service] = Service(service, services[service])

        return services


    def services(self):
        return list(self.service_list.values())
