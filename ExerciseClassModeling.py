
class Animal:
    """Animal Class"""
    def __init__(self, name):
        self.__CommonName = name
        
    @property
    def CommonName(self):
        return self.__CommonName
    
    @CommonName.setter
    def CommonName(self, name):
        self.__CommonName = name
        
    @property
    def Genus(self):
        return self.__Genus
    
    @Genus.setter
    def Genus(self, genus):
        self.__Genus = genus
          
    @property
    def Species(self):
        return self.__Species
    
    @Species.setter
    def Species(self, species):
        self.__Species = species
         
    @property
    def Subspecies(self):
        return self.__Subspecies
    
    @Subspecies.setter
    def Subspecies(self, Subspecies):
        self.__Subspecies = Subspecies
        
    @property
    def Weight(self):
        return self.__Weight
    
    @Weight.setter
    def Weight(self, Weight):
        self.__Weight = Weight
          
    @property
    def Height(self):
        return self.__Height
    
    @Height.setter
    def Height(self, Height):
        self.__Height = Height
          
    @property
    def Width(self):
        return self.__Width
    
    @Width.setter
    def Width(self, Width):
        self.__Width = Width

    def move(self, direction):
        print(f"Moving toward {direction}")
        distance = 0
        return distance
        
    def eat(self):
        print("eat")
        
    def sleep(self):
        print("sleep")
        duration = 0
        return duration


class Fish (Animal):
    """Fish Class"""    
    @property
    def Freshwater(self):
        return self.__Freshwater

    @Freshwater.setter
    def Freshwater(self, Freshwater):
        self.__Freshwater = Freshwater

    @property
    def Saltwater(self):
        return self.__Saltwater

    @Saltwater.setter
    def GenSaltwaters(self, Saltwater):
        self.__Saltwater = Saltwater

    @property
    def Edible(self):
        return self.__Edible

    @Edible.setter
    def Edible(self, Edible):
        self.__Species = Edible

    def swim(self, direction):
        print(f"Swimming toward {direction}")
        distance = self.move(direction)
        return distance

class Snake (Animal):
    """Snake Class"""
    @property
    def Venomous(self):
        return self.__Venomous

    @Venomous.setter
    def Venomous(self, Venomous):
        self.__Venomous = Venomous

    @property
    def SuitableAsPet(self):
        return self.__SuitableAsPet

    @SuitableAsPet.setter
    def SuitableAsPet(self, SuitableAsPet):
        self.__SuitableAsPet = SuitableAsPet
        
    def slither(self, direction):
        print(f"Slithering toward {direction}")
        distance = self.move(direction)
        return distance


class Person (Animal):
    """Person Class"""
    def __init__(self, name):
        self.__FullName = name
        
    @property
    def FullName(self):
        return self.__FullName

    @FullName.setter
    def FullName(self, FullName):
        self.__FullName = FullName
        
    @property
    def FirstName(self):
        return self.__FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self.__FirstName = FirstName
    @property
    def LastName(self):
        return self.__LastName

    @LastName.setter
    def LastName(self, LastName):
        self.__LastName = LastName

    def walk(self, direction):
        print(f"Walking toward {direction}")
        distance = self.move(direction)
        return distance
    

class Book :
    """Book Class"""

    def __init__(self, title):
        self.__Title = title

    @property
    def Title(self):
        return self.__Title

    @Title.setter
    def Title(self, title):
        self.__Title = title

    @property
    def Format(self):
        return self.__Format

    @Format.setter
    def Format(self, Format):
        self.__Format = Format
        
    def read(self, start_loc):
        print(f"Reading starting at {start_loc}")
        end_loc = start_loc
        return end_loc
        
class Textbook (Book):
    """Textbook Class"""

    @property
    def AuthorName(self):
        return self.__AuthorName

    @AuthorName.setter
    def AuthorName(self, AuthorName):
        self.__AuthorName = AuthorName

    @property
    def Publisher(self):
        return self.__Publisher

    @Publisher.setter
    def Publisher(self, Publisher):
        self.__Publisher = Publisher

    @property
    def PublishedDate(self):
        return self.__PublishedDate

    @PublishedDate.setter
    def PublishedDate(self, PublishedDate):
        self.__PublishedDate = PublishedDate

    @property
    def ISBN(self):
        return self.__ISBN

    @ISBN.setter
    def ISBN(self, ISBN):
        self.__ISBN = ISBN

    @property
    def ISBN13(self):
        return self.__ISBN13

    @ISBN13.setter
    def ISBN13(self, ISBN13):
        self.__ISBN13 = ISBN13

    def AnswerQuestions(self, number, page):
        print(f"Answer {number} {page}")
        answer = ""
        return answer


class AddressBook (Book):
    """AddressBook Class"""

    @property
    def OwnerName(self):
        return self.__OwnerName

    @OwnerName.setter
    def OwnerName(self, OwnerName):
        self.__OwnerName = OwnerName

    @property
    def Addresses(self):
        return self.__Addresses

    @Addresses.setter
    def Addresses(self, Addresses):
        self.__Addresses = Addresses

    def write(self, address):
        print(f"write {address}")
        return 
    
    def delete(self, address):
        print(f"Delete {address}")
        return    


class Vehicle:
    """Vehicle Class"""

    def __init__(self, Type):
        self.__Type = Type

    @property
    def ExteriorColor(self):
        return self.__ExteriorColor

    @ExteriorColor.setter
    def ExteriorColor(self, ExteriorColor):
        self.__ExteriorColor = ExteriorColor

    @property
    def InteriorColor(self):
        return self.__InteriorColor

    @InteriorColor.setter
    def InteriorColor(self, InteriorColor):
        self.__InteriorColor = InteriorColor

    def move(self, direction):
        print(f"Move in {direction}")
        distance = 0
        return distance
        
class Car (Vehicle):
    """Car Class"""

    def __init__(self, Make, Model, Year):
        self.__Make = Make
        self.__Model = Model
        self.__Year = Year

    @property
    def Make(self):
        return self.__Make

    @Make.setter
    def Make(self, Make):
        self.__Make = Make

    @property
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, Model):
        self.__Model = Model

    @property
    def Year(self):
        return self.__Year

    @Year.setter
    def AuthorYearName(self, Year):
        self.__Year = Year

    @property
    def VIN(self):
        return self.__VIN

    @VIN.setter
    def VIN(self, VIN):
        self.__VIN = VIN

    @property
    def Mileage(self):
        return self.__Mileage

    @Mileage.setter
    def Mileage(self, Mileage):
        self.__Mileage = Mileage

    @property
    def Engine(self):
        return self.__Engine

    @Engine.setter
    def Engine(self, Engine):
        self.__Engine = Engine

    @property
    def FuelType(self):
        return self.__FuelType

    @FuelType.setter
    def FuelType(self, FuelType):
        self.__FuelType = FuelType

    @property
    def Transmission(self):
        return self.__Transmission

    @Transmission.setter
    def Transmission(self, Transmission):
        self.__Transmission = Transmission

    @property
    def DriveTrain(self):
        return self.__DriveTrain

    @DriveTrain.setter
    def DriveTrain(self, DriveTrain):
        self.__DriveTrain = DriveTrain
        
        
    def drive(self, driverinput, wheelangle):
        print(f"drive {driverinput} {wheelangle}")
        speed = 0
        acceleration = 0
        return speed, acceleration
    
    def steer(self, driverinput):
        print(f"drive {driverinput}")
        wheelangle = 0
        return wheelangle


class Bicycle (Vehicle):
    """Bicycle Class"""
    
    def __init__(self, Type, CurrentGear):
        self.__Type = Type
        self.__CurrentGear = CurrentGear
        
    @property
    def NumWheels(self):
        return self.__NumWheels

    @NumWheels.setter
    def NumWheels(self, NumWheels):
        self.__NumWheels = NumWheels

    @property
    def NumGears(self):
        return self.__NumGears

    @NumGears.setter
    def NumGears(self, NumGears):
        self.__NumGears = NumGears
        
        
    def pedal(self, speed):
        print(f"Pedal {speed}")
        acceleration = 0
        return acceleration
    
    def steer(self, riderinput):
        print(f"steer {riderinput}")
        wheelangle = 0
        return wheelangle
    
    def shift(self, direction):
        print(f"shift {riderinput}")
        self.__CurrentGear += (1 if direction > 0 else -1)
        return self.__CurrentGear


class HotairBalloon (Vehicle):
    """HotairBalloon Class"""

    @property
    def Altitude(self):
        return self.__Altitude

    @Altitude.setter
    def Altitude(self, Altitude):
        self.__Altitude = Altitude

    @property
    def Capacity(self):
        return self.__Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self.__Capacity = Capacity

    def Vent(self, duration):
        print(f"vent {duration}")
        acceleration = 0
        return acceleration

    def burn(self, duration):
        print(f"burn {duration}")
        acceleration = 0
        return acceleration


class Boat (Vehicle):
    """Boat Class"""

    def __init__(self, VesselName):
        self.__VesselName = VesselName

    @property
    def ON(self):
        return self.__ON

    @ON.setter
    def ON(self, ON):
        self.__ON = ON

    @property
    def HIN(self):
        return self.__HIN

    @HIN.setter
    def HIN(self, HIN):
        self.__HIN = HIN

    @property
    def IMO(self):
        return self.__IMO

    @IMO.setter
    def IMO(self, IMO):
        self.__IMO = IMO

    @property
    def HailingPort(self):
        return self.__HailingPort

    @HailingPort.setter
    def HailingPort(self, HailingPort):
        self.__HailingPort  = HailingPort

    @property
    def Endorsements(self):
        return self.__Endorsements

    @Endorsements.setter
    def Endorsements(self, Endorsements):
        self.__Endorsements = Endorsements

    @property
    def PrimaryService(self):
        return self.__PrimaryService

    @PrimaryService.setter
    def EngiPrimaryServicene(self, PrimaryService):
        self.__PrimaryService = PrimaryService

    @property
    def Horsepower(self):
        return self.__Horsepower

    @Horsepower.setter
    def Horsepower(self, Horsepower):
        self.__Horsepower = Horsepower

    @property
    def VesselName(self):
        return self.__VesselName

    @VesselName.setter
    def VesselName(self, VesselName):
        self.__VesselName = VesselName


    def move(self, motor, rudder, wind, current):
        print(f"move {motor} {rudder} {wind} {current}")
        heading = 0
        speed = 0
        acceleration = 0
        return heading, speed, acceleration

    def steer(self, driverinput):
        print(f"drive {driverinput}")
        wheelangle = 0
        return wheelangle
