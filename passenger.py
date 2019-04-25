class Person:
    def __init__(self, name):
        self.name = name

class Passenger(Person):
    def __init__(self, name, passport_id):
        super().__init__(name)
        self.passport_id = passport_id

passenger_name = Person('Fred')
print(passenger_name.name)
