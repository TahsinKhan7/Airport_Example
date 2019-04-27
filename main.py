#Imports ALL from the flights file, including the previous import of passenger.
from flights import *

# General while loop to facilitate Airport flight adding program:
while True:

    #Title and user input request for 3 different flight class options
    print('\n What will you like to do?' '\n(State your chosen number)')
    user_input = int(input('\n 1)Add a passenger''\n 2)List of current flights' '\n 3)Add passenger to flight' '\n >>'))

    ##ADD A PASSENGER TO THE LIST
    if user_input == 1:
        print('Create a passenger')
        name = input('Please enter the passengers full name ')
        passport_id = input('Please enter the passport id ')
        obj_passenger.add_passenger(name, passport_id)

        #Request to see updated passenger list.
        see_passenger_list = input('See passenger list? (Y/N)')

        if see_passenger_list.strip().capitalize() == 'Y':
            #List header
            print('    Name -- Passport ID')

            #Prints Items in passenger list
            counter = 0
            for passanger in obj_passenger.passenger_list:
                print(counter + 1, ':', passanger)
                counter += 1
        else:
            break

    ##DISPLAY CURRENT FLIGHT LIST
    elif user_input == 2:
        print('----------------------------------------------------------')
        print(f'List of current flights for {obj_passenger.plane}:')

        counter = 0
        for flight in obj_flight.flight_list:
            print(counter + 1, ':', flight)
            counter += 1
        print('----------------------------------------------------------')

    #ADD CURRENT PASSENGERS TO FLIGHT LIST:

    elif user_input == 3:

        #Starting statement/Title
        print('\n You have chosen to add a passenger to a flight.\n')

        # Below prints the current flight list and plane:
        print(f'List of current flights for {obj_passenger.plane}:')

        counter = 0
        for flight in obj_flight.flight_list:
            print(counter, ':', flight)
            counter += 1

        #Len will be used to check for correct user input of selections:
        flight_list_len = len(obj_flight.flight_list)

        #Asks user to select from the just printed flight list:
        select_flight = int(input('\nWhich flight would you like to add a passenger to?').strip())

        print(f'\nYou have selected to add a passenger to flight: {obj_flight.flight_list[select_flight]}\n')

        #If statement below passes if the users input is within the length of the list:
        if select_flight <= int(flight_list_len) and select_flight >= 0:

            #Equates the users selected flight to a 'selected_flight' variable
            selected_flight = obj_flight.flight_list[select_flight]

            #Prints passenger list:
            counter = 0
            for passanger in obj_passenger.passenger_list:
                print(counter, ':', passanger)
                counter += 1
            passenger_len = len(obj_flight.flight_list)

            #Asks user to select from passenger list:
            select_passenger = (int(input('\n Which passenger would you like to add? \n').strip()))

            # IF statement passes if user input is within the length of the list
            if select_passenger <= int(passenger_len) and select_passenger >= 0:

                #Stores the selected passenger element to a 'selected_passenger' variable:
                selected_passenger = obj_passenger.passenger_list[select_passenger]

                #Extrapolates selected passenger to flight list object:
                obj_flight.flight_list.insert(select_flight+1, '  >>> Passenger: ' + selected_passenger + '')

                #Replace index element method:
                #obj_flight.flight_list[select_passenger] = selected_flight + '\n       [' + selected_passenger + ']'

            else:
                print('Please pick the correct number from the available passenger list.')

        else:
            print('Please pick a flight number from the available flight list.')

        #Prints updated flight list with now added passengers:
        updated_flight_list = input('\n See updated flight list? (Y/N)').strip().capitalize()

        if updated_flight_list.strip().capitalize() == 'Y':
            #counter = 0
            for flight in obj_flight.flight_list:
                print(flight)
                #counter += 1
        else:
            break
    else:
        print('Please input one of the available option numbers')

 # list of flights
        # (I can use code from option 2)
        # prompt user for input and store in variable(what flight will you like to go to?
        # use the number to get a flight object out of the flight list flight_list[user_input]
        # call .add_passenger method on the flight object
        # send in a passenger object (create one or select from a list)