from Unit import Unit

class Archer(Unit):

    def __init__(self):
        self.unit_name = "Knight"
        self.unit_cost = 800
        self.unit_health_default = 4000
        self.unit_power_default = 700
        self.unit_status = "Alive"

