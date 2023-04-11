class Bus:
    def __init__(self, input_route_number, input_destination):
        self.route_number = input_route_number
        self.destination = input_destination
        self.passengers = []

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, Person):
        self.passengers.append(Person)

    def drop_off(self, Person):
        self.passengers.remove(Person)

    def empty_bus(self):
        if self.passengers:
            self.passengers.clear()

    

        
    
