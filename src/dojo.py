class Dojo:
    pass

class Person(Dojo):
    def __init__(self,name):
        #Dojo.__init__(self,allocations,all_persons)
        self.name = name
        
    def add_person(self,role,wants_accomodation="N"):
        self.role = role
        self.wants_accomodation = wants_accomodation
        office = []
        living = []
        all_persons = []
        if self.role == "Staff":
            wants_accomodation = "N"
            office.append(self.name)
            all_persons.append(self.name)
        all_persons.append(self.name)
        office.append(self.name)
        living.append(self.name)
        if self.role == "Staff" and self.wants_accomodation == "Y":
            return "A staff cannot be allocated living space"
        if self.wants_accomodation == "Y":
            return "The {} {} has been created and allocated office {} and living space {}".format(self.role,self.name,office[0],living[0])
        return "The {} {} has been created and allocated office {}".format(self.role,self.name,office[0])
       

class Fellow(Person):
    """Inherits from Person"""
    def __init__(self, name):
        super().__init__(name, role="Fellow")
	
class Staff(Person):
    """Inherits from Person"""
    def __init__(self, name):
        super().__init__(name, role="Staff")

class Room(Dojo):
    def __init__(self, room_type, room_name):
        self.room_type = room_type
        self.room_name = room_name
    def create_room(self):
        if self.room_type == "Office":
            return "The {} {} was created.".format(self.room_type, self.room_name.upper())
        elif self.room_type == "Living Space":
            return "The {} {} was created.".format(self.room_type, self.room_name.upper())
        else:
            return "No such room can be created"

class Office(Room):
    """Inherits from Room"""
    def __init__(self, room_type, room_name):
        super().__init__(room_name, room_type = "Office")
class LivingSpace(Room):
    """Inherits from Room"""
    def __init__(self, room_type, room_name):
        super().__init__(room_name, room_type = "Living Space")

