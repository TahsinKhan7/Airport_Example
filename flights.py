from passenger import *

class Flight:
    def __init__(self):
        self.origin = ""
        self.destination = ""
        self.plane = ""
        self.passenger_list = []
    # has a origin
    # has a destination
    # has a list to keep passenger objects
    # has a plane
    # create a method to add 1 passenger to the list of passengers
    # create another method to add a plane

    def add_passenger(self, name):
        self.passenger_list.append(name)
        return self.passenger_list

    def add_plane(self, plane):
        self.plane = plane
        return self.plane

    def add_origin(self, origin):
        self.orgin = origin
        return self.origin

    def add_destination(self, destination):
        self.destination = destination
        return self.destination


test_flight = Flight()
test_flight.add_plane('Plane 1')
test_flight.add_origin('London')
test_flight.add_destination('LA')
test_flight.add_passenger('Fred')

person = Passenger('Leo', '89yr29r')
print(person.name)


#Adding a passenger 1 - as an object - Step by step
# Step 1 - Create a flight
# Step 2= Create a passenger object
# Save the passenger in a variable

#Step 3 = on the flight obj call the add_passenger() method:
test_flight.add_passenger(person)
#Send in the pasenger object as the arguemtnt
# This gives a list with on passenger object.

print(test_flight.add_plane('Easy Jet'))
