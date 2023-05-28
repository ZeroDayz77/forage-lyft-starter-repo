from abc import ABC, abstractmethod


class ServiceableInterface:
    def __init__(self):
    
    @abstractmethod
    def need_service(self):
        pass
