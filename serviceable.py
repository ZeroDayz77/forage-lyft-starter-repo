from abc import ABC, abstractmethod


class ServiceableInterface(ABC):
    
    @abstractmethod
    def need_service(self):
        pass
