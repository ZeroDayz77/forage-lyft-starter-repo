from serviceable import ServiceableInterface

class Car(ServiceableInterface):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
        
    
    def needs_service(self):
        pass
