class Car:
    def __init__(self):
        self.make = " "
        self.year = " "
        self.plateNumber = " "
    
    def setName(self, name):
        self.name = name
    def setYear(self, year):
        self.year = int(year)
    def setPlateNumber(self, plateNumber):
        self.plateNumber = int(plateNumber)
    def setAllValuesOnce(self, name, year, plateNumber):
        self.name = name
        self.year = year
        self.plateNumber = plateNumber

    def getName(self):
        return self.name
    def getyear(self):
        return self.year
    def getPlateNumber(self):
        return self.plateNumber
    def displayCar(self):
        print(f"Car details: {self.getName()} {self.getyear()}, {self.getPlateNumber()}")

    def compareModel(self, b):
        if int(self.year) > int(b.year):
            print(f"{self.name} is older than {b.name}.")
        elif int(self.year) < int(b.year):
            print(f"{self.name} is newer than {b.name}.")
        else:
            print(f"Both cars were made in the same year")


class ElectricCar(Car):
    def __init__(self, battery):
        super().__init__()
        self.battery = battery
    
    def getBattery(self):
        return self.battery

    def displayCar(self):
        print(f"Car details: {self.getName()} {self.getyear()}, {self.getPlateNumber()}, {self.getBattery()}")

#main
car1 = Car()
car1.setName("Mercedes")
car1.setYear(2020)
car1.setPlateNumber(2020083010)
car1.displayCar()

#electric car object
car2 = ElectricCar("Tiger battery")
car2.setName("Tesla")
car2.setYear(2020)
car2.setPlateNumber(20200830400)
car2.displayCar()

#make comparison based on year of manufacture
car1.compareModel(car2)
