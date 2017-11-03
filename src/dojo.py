office = ''
living = ''
all_rooms = {}
class Dojo:
    def __init__(self):
        pass
        #self.all_persons = []
      
class Room(Dojo):
    def __init__(self, room_type, room_name):
        self.room_type = room_type
        self.room_name = room_name
       
    def create_room(self):
        if self.room_type == "Office":
            all_rooms["Office"] = self.room_name
            office = all_rooms['Office']
            return "The {} {} was created.".format(self.room_type, self.room_name.upper())
        elif self.room_type == "Living Space":
            all_rooms["Living Space"] = self.room_name
            living = all_rooms["Living Space"] 
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

class Person(Dojo):
    def __init__(self,name,all_persons = None):
        #Dojo.__init__(self,all_persons)
        self.all_persons = []
        self.name = name
    
    def add_person(self,role,wants_accomodation="N"):
        self.role = role
        self.wants_accomodation = wants_accomodation
        office = []
        living = []
        if self.role == "Staff":
            wants_accomodation = "N"
            office.append(self.name)
            self.all_persons.append(self.name)
        self.all_persons.append(self.name)
        office.append(self.name)
        living.append(self.name)
        if self.role == "Staff" and self.wants_accomodation == "Y":
            return "A staff cannot be allocated living space"
        if self.wants_accomodation == "Y":
            return "The {} {} has been created and allocated office {} and living space {}".format(self.role,self.name,all_rooms["Office"] , all_rooms["Living Space"])
        return "The {} {} has been created and allocated office {}".format(self.role,self.name,all_rooms["Office"] )
       

class Fellow(Person):
    """Inherits from Person"""
    def __init__(self, name):
        super().__init__(name, role="Fellow")
	
class Staff(Person):
    """Inherits from Person"""
    def __init__(self, name):
        super().__init__(name, role="Staff")

''' 
j = Room("Living Space", "ruby")
print(j.create_room())
j = Room("Office", "Production")
print(j.create_room())
j = Person("justin ndwiga")
print(j.add_person("Fellow","Y")) '''