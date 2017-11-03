class Room(object):
    '''
    The Room class models the rooms in Dojo and
    is used as the blueprint for how the LivingSpace
    and OfficeSpace classes inehrit properties such
    as room_name,room_type and capacity.s
    '''

    def __init__(self, room_name, room_type, capacity):
        self.room_type = room_type.strip().title()
        self.capacity = capacity
        self.room_name = room_name.title()
        self.occupants = []

    def add_person(self, person):
        '''
        This is what will check capacity and reduce
        by one when someone is added to a room.
        '''
        self.occupants.append(person)
        self.capacity = self.capacity - 1
        return self.capacity


class LivingSpace(Room):
    '''
    The LivingSpace class inherits its properties and
    methods from the Room class and overrides properties
    such as capacity using the super function call.
    '''
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(
            room_name, room_type='Living Space', capacity=4)


class Office(Room):
    '''
    The Office class inherits its properties and
    methods from the Room class and overrides properties
    such as capacity using the super function call.
    '''
    def __init__(self, room_name):
        super(Office, self).__init__(room_name, room_type='Office', capacity=6)