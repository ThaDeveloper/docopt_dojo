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
    pass
class Office(Room):
    pass
class LivingSpace(Room):
    pass
j = Person("justin ndwiga")
print(j.add_person("Fellow","N"))
