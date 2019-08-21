"""Service object."""

class Service:
    def __init__(self, name, data):
        self.name = name

        self.owner = data["owner"]
        self.technologies = data["technologies"]
