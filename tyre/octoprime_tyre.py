from tyre.tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, tyre_wear):
        self.tyre_wear = tyre_wear[0,0,0,0]
    
    
    def needs_service(self):
        for x in self.tyre_wear:
            if x >= 0.9:
                return True
            else:
                return False