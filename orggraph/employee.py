class Employee:
    def __init__(self, name, data):
        self.name = name

        self.role = data["is_a"]
        self.member_of = data["member_of"]
        self.aliases = data.get("aliases", [])

        self.manager = None

        self.assigned_to = data.get("assigned_to", [])
        self.manages = data.get("manages", [])

    def set_manager(self, manager):
        self.manager = manager

    def get_manager(self):
        return self.manager
