class Person(object):
    '''
    The Person class models the rooms in Dojo and
    is used as the blueprint for how the LivingSpace
    and OfficeSpace classes inehrit properties such
    as room_name,room_type and capacity
    '''

    def __init__(self, first_name, last_name, person_type):
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.person_type = person_type.strip().title()
        self.accomodate = 'N'

    def get_full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        self.full_name = full_name

    def assign_identifier(self, identifier):
        self.identifier = identifier


class Fellow(Person):
    def __init__(self, first_name, last_name):
        super(Fellow, self).__init__(
            first_name, last_name, person_type='Fellow')


class Staff(Person):
    def __init__(self, first_name, last_name):
        super(Staff, self).__init__(
