from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod # no obj needed for abstract method
    def start(self):
        pass
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Starting")
    def stop(self):
        print("Stopping")
ob=Car()
ob.start()
ob.stop()
