from passenger import *

class Flight:
    def __init__(self, origin_destination='', plane=''):
        self.plane = plane
        self.passenger_list = []
        self.origin_destination = origin_destination
        self.flight_list = []
        self.flight_with_passenger = []

    def add_passenger(self, name, passport_id):
        self.passenger_list.append(name + ' --' + ' ' + 'id: ' + passport_id)
        #return self.passenger_list

    def add_plane(self, plane):
        self.plane = plane
        return self.plane

    def add_flight(self, origin_destination):
        self.flight_list.append(origin_destination)
        #return self.flight_list


###Setting passenger class instance (Instanciating/Objectifying)###
obj_passenger = Flight()

#Adding a plane object
obj_passenger.add_plane('British Airways')
print('Plane:', obj_passenger.plane)

### Creating passenger name & id objects through the arguments of Passenger(name, id)
person_1 = Passenger('Jon Snow', '28938')          #use print(person_1.name) to print name
person_2 = Passenger('Arya Stark', '166826')
person_3 = Passenger('Sansa Stark', '185826')
person_4 = Passenger('Rob Stark', '126476')
person_5 = Passenger('Ned Stark', '349289')

##Passing defined person objects above through add_passenger method to augment into defined self.flight list
#(Send in the pasenger object as the arguemtnt) (# This gives a list with on passenger object.)
obj_passenger.add_passenger(person_1.name, person_1.passport_id)
obj_passenger.add_passenger(person_2.name, person_2.passport_id)
obj_passenger.add_passenger(person_3.name, person_3.passport_id)
obj_passenger.add_passenger(person_4.name, person_4.passport_id)
obj_passenger.add_passenger(person_5.name, person_5.passport_id)

#####Printing each of the passengers in the passenger list:####
# print('    Name -- Passport ID')
# counter = 0
# for passanger in obj_passenger.passenger_list:
#     print(counter + 1, ':', passanger)
#     counter += 1


##### Flight List######
#Class instance for adding flights
obj_flight = Flight()

#Instantiating/objectifying flights into the flight class
flight_1 = Flight('London to LA')
flight_2 = Flight('Madrid to Tokyo')
flight_3 = Flight('Paris to Sydney')
flight_4 = Flight('Egypt to Berlin')
flight_5 = Flight('New York to Moscow')


## Passing instance flight objects through add_flight method to add each flight to defined flight list.
obj_flight.add_flight(flight_1.origin_destination)
obj_flight.add_flight(flight_2.origin_destination)
obj_flight.add_flight(flight_3.origin_destination)
obj_flight.add_flight(flight_4.origin_destination)
obj_flight.add_flight(flight_5.origin_destination)


###Printing flight list#############
# print('')
# print('Current Flights:')
# counter = 0
# for flight in obj_flight.flight_list:
#     print(counter + 1, ':', flight)
#     counter += 1