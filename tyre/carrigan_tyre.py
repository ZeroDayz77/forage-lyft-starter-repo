from tyre.tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, tyre_wear):
        self.tyre_wear = tyre_wear[0] * 4
    
    
    def needs_service(self):
        sum = 0
        
        for x in self.tyre_wear:
            sum += x
        if sum >= 3:
            return True
        else:
            return False