class Computer:
    def __init__(self):
        self.name = None
        self.price = None
        self.processor = None
        self.ram = None
        self.os = None
        self.hdd = None
        
    def __str__(self):
        return f"{self.name}: {self.price}$, {self.processor}, {self.ram}GB RAM, {self.os}, {self.hdd}GB HDD"
    
class ComputerBuilder:
    
    def __init__(self):
        self.computer = Computer ()

    def build_name(self, name):
        self.computer.name = name
        return self
    
    def build_price(self, price):
        self.computer.price = price
        return self
    
    def build_processor(self, processor):
        self.computer.processor = processor
        return self
    
    def build_ram(self, ram):  
        self.computer.ram = ram
        return self
    
    def build_os(self, os):
        self.computer.os = os
        return self
    
    def build_hdd(self, hdd):
        self.computer.hdd = hdd
        return self
    
    def get_computer(self):
        return self.computer
    
class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder
    
    def construct_computer(self):
        self.builder.build_name("Laptop").build_price(1200).build_processor("Intel i7").build_ram(16).build_os("Windows 10").build_hdd(512)
        return self.builder.get_computer()
    
    def construct_gaming_computer(self):
        self.builder.build_name("Gaming PC").build_price(2500).build_processor("AMD Ryzen 9").build_ram(32).build_os("Windows 11").build_hdd(1024)
        return self.builder.get_computer()
    
    def construct_laptop(self):
        self.builder.build_name("Lenovo LOQ").build_price(1500).build_processor("Intel i5").build_ram(8).build_os("Windows 10").build_hdd(256)
        return self.builder.get_computer()

builder = ComputerBuilder()
director = ComputerDirector(builder)
gaming_pc = director.construct_gaming_computer()
print(gaming_pc)

laptop = director.construct_laptop()
print(laptop)