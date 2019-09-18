class Employee:
    def __init__(self, employee_id, data):
        self.employee_id = employee_id
        self.data = data

        self.name = data["name"]

        self.job_title = data["job_title"]
        self.department = data["department"]
        self.aliases = data.get("aliases", [])
        self.tech_leads = data.get("tech_lead", [])

        self.manager = None

        self.teams = data.get("teams", [])
        self.manages = data.get("manages", [])

        self.node_id = None

    def set_manager(self, manager):
        self.manager = manager

    def get_manager(self):
        return self.manager

    def get_data(self):
        return self.data
