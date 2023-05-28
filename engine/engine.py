from car import Car

class Engine(Car):
    class WilloughbyEngine(Car):
        def __init__(self, current_mileage, last_service_mileage):
            self.current_mileage = current_mileage
            self.last_service_mileage = last_service_mileage

        def needs_service(self):
            return self.current_mileage - self.last_service_mileage > 60000
    
    
    class SternmanEngine(Car):
        def __init__(self, warning_light_is_on):
            self.warning_light_is_on = warning_light_is_on

        def needs_service(self):
            if self.warning_light_is_on:
                return True
            else:
                return False
    
    
    class CapuletEngine(Car):
        def __init__(self, current_mileage, last_service_mileage):
            self.current_mileage = current_mileage
            self.last_service_mileage = last_service_mileage

        def needs_service(self):
            return self.current_mileage - self.last_service_mileage > 30000