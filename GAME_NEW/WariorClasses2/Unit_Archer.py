from Unit import Unit

class Archer(Unit):

    def __init__(self):
        self.unit_name = "Archer"
        self.unit_cost = 1000
        self.unit_health_default = 3000
        self.unit_power_default = 800
        self.unit_status = "Alive"

