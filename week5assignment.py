from abc import ABC, abstractmethod

class Exchanger(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def exchange(self, value):
        pass
    def describe(self, value):
        exchanged = self.exchange(value)
        result = f"{self.name}: {value} -> {exchanged}"
        return result
        
class USDToEUR(Exchanger):
    def __init__(self):
        super().__init__("USDToEUR")
    def exchange(self, value):
        result = round(value * 0.9216, 2)
        return result

class USDToGBP(Exchanger):
    def __init__(self):
        super().__init__("USDToGBP")
    def exchange(self, value):
        result = round(value * 0.7893, 2)
        return result
    
class USDToJPY(Exchanger):
    def __init__(self):
        super().__init__("USDToJPY")
    def exchange(self, value):
        result = round(value * 149.52, 2)
        return result

class CustomExchanger:
    def __init__(self,name,rate):
        self.name = name
        self.rate = rate
    def exchange(self, value):
        result = round(value * self.rate, 2)
        return result
    def describe(self, value):
        exchanged = self.exchange(value) 
        result = f"{self.name}: {value} -> {exchanged}"
        return result

class ExchangeLog:
    def __init__(self):
        self.entries = []
    def record(self, exchanger_name, original, exchanged):
        entry = f"{exchanger_name}: {original} -> {exchanged}"
        self.entries.append(entry)
        result = entry
        return result
    def show(self):
        for entry in self.entries:
            print(entry)
        result = None
        return result 

class ExchangeDesk:
    def __init__(self,name):
        self.exchangers = []
        self.name = name 
        self.log = ExchangeLog()
    def add_exchanger(self,exchanger):
        self.exchangers.append(exchanger)
        result = None
        return result
    def exchange_all(self, value):
        print(f"=== {self.name} ===")
        for exchangers in self.exchangers:
            description = exchangers.describe(value)
            print(description)
            exchanged_value = exchangers.exchange(value)
            self.log.record(exchangers.name, value, exchanged_value)
        result = None
        return result
    def show_log(self):
        print(f"--- Log for {self.name} ---")
        self.log.show()
        result = None
        return result
    
desk = ExchangeDesk('Airport Kiosk')
desk.add_exchanger(USDToEUR())
desk.add_exchanger(USDToGBP())
desk.add_exchanger(USDToJPY())
desk.add_exchanger(CustomExchanger('USDToUZS', 12850.0))

desk.exchange_all(200)
print()
desk.exchange_all(75)
print()
desk.show_log()

try:
    e = Exchanger('test')
except TypeError:
    print('Cannot instantiate abstract class')
