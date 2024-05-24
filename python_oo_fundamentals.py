# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle 
# with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.

# Expected Outcome: Completion of the Vehicle
# class with the update_owner method 
# and a demonstration script showing the creation of 
# Vehicle objects and updating their owners.

class Vehicle:
    def __init__(self, registrationNum, type, owner):
        self.registrationNum = registrationNum
        self.type = type
        self.owner = owner

    def updateOwner(self, owner):
        self.owner = owner
print("{:>80}".format("*********REGISTRATION SYSTEM*********\n"))
owner1 = Vehicle("1000", "Camero", "Devin")
print(f"PREVIOUS OWNER #1: {owner1.owner}")
owner1.updateOwner("Halo")
print(f"UPDATED OWNER #1: {owner1.owner}")
print()
owner2 =  Vehicle("1001", "Jeep Patriot", "Willow")
print(f"PREVIOUS OWNER #2: {owner2.owner}")
owner2.updateOwner("Ben")
print(f"UPDATED OWNER #2: {owner2.owner}")
print()
owner3 =  Vehicle("1001", "Tesla", "Flash")
print(f"PREVIOUS OWNER #3: {owner3.owner}")
owner3.updateOwner("Tim")
print(f"UPDATED OWNER #3: {owner3.owner}")
print()

# Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by 
# adding a feature to keep track of the number of participants. 
# Implement a method add_participant that increases the count and 
# a method get_participant_count to retrieve the current count.
print("{:>83}".format("*********EVENT MANAGEMENT SYSTEM*********\n"))
class Event:
    
    def __init__(self, name, date):
        self.name = name
        self.date = date   
        self.counter = 0

    def addParticipant(self):
        self.counter += 1

    def getNumParticipants(self):
        return self.counter

event1 = Event("Juneteenth", "2024-19-06")
event1.addParticipant()
event1.addParticipant()
event1.addParticipant()
event1.addParticipant()
print(f"NUMBER OF PARTICIPANTS TO ATTEND {event1.name.upper()}: {event1.getNumParticipants()}")
print(f"EVENT SET FOR: {event1.date}\n")

# Task 1: File Handling for Building Records

# Problem Statement: Implement a system to handle 
# building records using file operations. Create a Building 
# class and write a script to save and load building details 
# to and from a file.

# Expected Outcome: A complete Building class with 
# methods for saving to and loading details from a 
# file. A script demonstrating saving multiple 
# buildings to a file and then reading them back into the program.
print("{:>80}".format("*********BUILDING RECORDS*********\n"))

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def saveToFile(self):
        data = f"BUILDING NAME: {self.name.upper()} | FLOORS: {self.floors}"
        with open("building_info.txt", "w") as file:
            print("SAVING TO FILE...\n")
            file.write(data)

    def loadFromFile(self):
        with open("building_info.txt", "r") as file:
            data = file.readlines()
            print(" ".join(data))

building1 = Building("Twin Tower".upper(), 108)
building1.saveToFile()
building1.loadFromFile()
print()
# Task 1: Public Transportation Module

# Problem Statement: Develop a Bus class as part of a public transportation
# module. Use class variables to represent common attributes like city 
# name and base fare. Implement instance variables for specific attributes 
# like route number and passenger capacity.

# Expected Outcome: A Bus class with both class and instance variables, 
# and a transportation module to manage different bus routes. A test script 
# should demonstrate creating bus instances and accessing both class and instance attributes.
print("{:>90}".format("*********PUBLIC TRANSPORTATION INFORMATION*********\n"))
from transportation_module import Bus

route1 = Bus(250, 50)
print(f"ROUTE {route1.routeNum} IN {route1.city.upper()} HAS CAPACITY FOR {route1.passengerCapacity} PASSENGERS AT ${route1.baseFare:.2f}")

route2 = Bus(350, 75)
print(f"ROUTE {route2.routeNum} IN {route2.city.upper()} HAS CAPACITY FOR {route2.passengerCapacity} PASSENGERS AT ${route2.baseFare:.2f}")
    
print()
