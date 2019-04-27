from passenger import *

class Flight:
    def __init__(self, origin_destination=''):
        self.plane = ""
        self.passenger_list = []
        self.origin_destination = origin_destination
        self.flight_list = []

    def add_passenger(self, name):
        self.passenger_list.append(name)
        return self.passenger_list

    def add_plane(self, plane):
        self.plane = plane
        return self.plane

    def add_origin_destination(self, origin_destination):
        self.flight_list.append(origin_destination)
        return self.flight_list

test_flight = Flight()
test_flight.add_plane('Easy Jet')
test_flight.add_origin_destination('London to LA')
test_flight.add_passenger('Fred')

person_1 = Passenger('Jon Snow', '136826')
print(person_1.name)
person_2 = Passenger('Arya Stark', '166826')
print(person_2.name)
person_3 = Passenger('Sansa Stark', '185826')
print(person_3.name)
person_4 = Passenger('Rob Stark', '126476')
print(person_4.name)
person_5 = Passenger('Ned Stark', '349289')
print(person_5.name)

#Adding a passenger 1 - as an object - Step by step
# Step 1 - Create a flight
# Step 2= Create a passenger object
# Save the passenger in a variable

#Step 3 = on the flight obj call the add_passenger() method:
##### NOTE REMOVE .name from below to print object memory number!!!###
test_flight.add_passenger(person_1.name)
test_flight.add_passenger(person_2.name)
test_flight.add_passenger(person_3.name)
test_flight.add_passenger(person_4.name)
test_flight.add_passenger(person_5.name)
#Send in the pasenger object as the arguemtnt
# This gives a list with on passenger object.

print(test_flight.add_plane('British Airways'))

print(test_flight.passenger_list)

#flight list
#flight_list = []


##################
while True:
    print('What will you like to do? (insert corresponding number)')
    user_input = input('\n 1)Add a passanger''\n 2)List of current flights' '\n 3)Add passenger to flight list' '\n >>')

    if user_input == 1:
        print('Create a passenger')
        name = input('Please enter the passengers name')
        passport_id = input('Please enter the passport id')
        Passenger(name, passport_id)
        #gender = input('Please enter gender')
        #national
    elif user_input == str(2):
        print('List of flights')

        for flight in :
            print(flight.add_origin_destination)
    else:
        print('please input the correct number')






















# while Tru
#     print('\n 1) create a passanger \n 2) list flights \n 3) add passenge to exiting flight
# if ===1
#     print('you are now in option 1')
#     name = input(whats the passengers name)
#     passport
#     gender
#     Passenger(name, passport, gender, 'british')
# elif user impot==2
#     for flight in flight list
#             print(destination: flight.destination)
# elif user_input==3
#
# else
#
# passport
# gender
# Passenger()


