#click - cli package that for our case will be used to printout screen messages
from random import randint
import click
from src.room import LivingSpace, Office
from src.person import Fellow, Staff


class Dojo(object):
    '''
    Dojo is the main class that uses the imported
    inherited classes:
    1.LivingSpace, Office ---> Room
    2.Staff, Fellow ---> Person
    This class instantiates the above sub classes and
    appropriately performs operations from them.
    '''

    def __init__(self):
        self.offices = {
            'available': [],
            'unavailable': []
        }
        self.living_spaces = {
            'available': [],
            'unavailable': []
        }
        self.rooms = []
        self.fellows = []
        self.staff = []
        self.people = self.staff + self.fellows
        self.f_ids = [0]
        self.s_ids = [0]
        # # Regarding allocations
        self.staff_allocations = []
        self.fellow_allocations = []
        self.unallocated_persons = []

    def create_room(self, room_type, room_name):
        '''
        The create_room method in the dojo class takes
        in room_type and room_name and instantiates those rooms.
        An office is created as an instance of the Office class.
        A living space is created as an instance of the LivingSpace class.
        -->The single room dictionary holds information regarding
        a specific single room and appends this to the rooms
        list
        '''
        if not isinstance(room_type, str) or room_type.upper() not in ['O', 'L']:
            click.secho('Error.Please enter O or L for a room type.',
                        bold=True, fg='red')
            return 'Error. Invalid room type initial.'
        room_type = room_type.strip().upper()
        room_name = room_name.strip().capitalize()
        if room_type == 'O':
            room_type = 'Office'
        elif room_type == 'L':
            room_type = 'Living Space'
        for room in self.rooms:
            if room.room_name == room_name and \
                    room.room_type == room_type:
                click.secho('%s %s ALREADY EXISTS.Please pick another name.'
                            % (room_type, room_name),
                            fg='red', bold=True)
                return 'Room already exists.'
        if room_type == 'Office':
            room = Office(room_name)
            self.offices['available'].append(room.room_name)
        elif room_type == 'Living Space':
            room = LivingSpace(room_name)
            self.living_spaces['available'].append(room.room_name)
        self.rooms.append(room)
        click.secho('The %s %s has been created.' %
                    (room.room_type, room.room_name), bold=True, fg='green')
        return 'Room %s created.' % room.room_name

    def validate_person(self, first_name, last_name, role,
                        accomodate='N'):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            click.secho('Incorrect name type format.', fg='red')
            return 'Wrong type for name.'
        elif role.capitalize() not in ['Fellow', 'Staff']:
            click.secho('Please enter either Fellow or Staff for role',
                        fg='red', bold=True)
            return 'Invalid role'
        elif accomodate.upper() not in ['Y', 'N']:
            click.secho('Please enter Y or N for wants accomodation?',
                        fg='red', bold=True)
            return 'Wants accomodation not Y or N'
        accomodate = accomodate.upper()
        role = role.capitalize()
        if role == 'Staff' and accomodate == 'Y':
            accomodate = 'N'
            click.secho(
                'A Staff member cannot be allocated accomodation. \
                An office will however be allocated.',
                fg='red', bold=True)
        fn = first_name.capitalize() + ' ' + last_name.capitalize()
        for person in self.people:
            if person.full_name == fn and \
                    person.role == role.capitalize():
                click.secho('%s %s ALREADY EXISTS.' % (role, fn), fg='red', bold=True)
                return 'Person exists.'
        if not self.offices['available'] and role == 'Staff':
            click.secho(
                'There are no offices or the offices are all full.',
                fg='red', bold=True)
            #return 'There are no offices in the system.'
        elif not self.offices['available'] and role == 'Fellow':
            click.secho(
                'There are no offices or the offices are all full.',
                fg='red', bold=True)
            #return 'There are no offices in the system.'
        elif accomodate == 'Y' and role == 'Fellow':
            if not self.living_spaces['available'] and not \
                self.offices['available']:
                click.secho('THERE ARE NO ROOMS IN THE SYSTEM YET OR ALL ROOMS ARE FULL.',
                            fg='red', bold=True)
                #return 'There are no rooms in the system.'
            elif not self.living_spaces['available']:
                msg = 'Please add a living space for a fellow '
                msg += 'to be allocated both room types.'
                click.secho(msg, fg='red', bold=True)
                #return 'No Living space for fellow requiring both.'
            elif not self.offices['available']:
                msg = 'Please add an office for a fellow '
                msg += 'to be allocated both room types.'
                click.secho(msg, fg='red', bold=True)
                #return 'No office for fellow requiring both.'
        return [fn, accomodate, role]

    def generate_identifier(self, validated_details):
        fn = validated_details[0]
        accomodate = validated_details[1]
        role = validated_details[2]
        full_names = fn.split()
        if not self.people:
            if role.capitalize() == 'Fellow' or role.capitalize() == 'Staff':
                f_id = 1
                self.f_ids.append(f_id)
                identifier = 'F' + str(f_id)
                person = Fellow(full_names[0], full_names[1])
                person.accomodate = accomodate
                person.get_full_name()
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
            elif role.capitalize() == 'Staff':
                s_id = 1
                self.s_ids.append(s_id)
                identifier = 'S' + str(s_id)
                person = Staff(full_names[0], full_names[1])
                person.accomodate = accomodate
                person.get_full_name()
                person.assign_identifier(identifier)
                self.staff.append(person.full_name)
        else:
            if role.capitalize() == 'Fellow':
                person = Fellow(full_names[0], full_names[1])
                person.accomodate = accomodate
                person.get_full_name()
                f_id = self.f_ids.pop() + 1
                identifier = 'F' + str(f_id)
                self.f_ids.append(f_id)
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
            elif role.capitalize() == 'Staff':
                person = Staff(full_names[0], full_names[1])
                person.accomodate = accomodate
                person.get_full_name()
                s_id = self.s_ids.pop() + 1
                identifier = 'S' + str(s_id)
                self.s_ids.append(s_id)
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
        self.people.append(person)
        click.secho('The %s %s has been added.' %
                    (person.role, person.full_name),
                    fg='green', bold=True)
        return person

    def get_identifier(self, first_name, last_name):
        """
        The get identfier method intends to get a person's
        id to be able to reallocate them appropriately.
        """
        if not self.people:
            click.secho('There are Currently no people in the system.')
            return 'No people added'
        else:
            fn = first_name.title() + ' ' + last_name.title()
            for person in self.people:
                if person.full_name == fn:
                    msg = click.secho(person.identifier, fg='green')
                    return person.identifier
            else:
                msg = click.secho('Person does not exist.', fg='red')
                return msg

    def allocate_room(self, person):
        # random allocation
        # only a fellow can be allocated a living space
        # a staff can only be allocated an office.
        if person.role == 'Staff':
            if len(self.offices['available']) == 0:
                return self.unallocated_persons.append(person.full_name)
            staff_single_allocation = {}
            staff_single_allocation[person.full_name] = self.offices['available'][
                randint(0, (len(self.offices['available']) - 1))]
            self.staff_allocations.append(staff_single_allocation)
            for room in self.rooms:
                if room.room_name == staff_single_allocation[person.full_name]:
                    if room.capacity > 0:
                        room.capacity = room.add_person(person.full_name)
                    else:
                        self.offices['available'].remove(room.room_name)
                        self.offices['unavailable'].append(room.room_name)
                        self.unallocated_persons.append(person.full_name)
                        msg = '%s has reached its Maximum capacity.' % room.room_name
                        msg += 'Please add another %s.' % room.room_type
                        click.secho(msg, fg='red', bold=True)
            return click.secho('Staff %s has been allocated office %s'\
                        %(person.full_name, staff_single_allocation[person.full_name]), fg='green')

        elif person.role == 'Fellow':
            if person.accomodate == 'Y':
                if len(self.living_spaces['available']) == 0 or len(self.offices['available']) == 0:
                    return self.unallocated_persons.append(person.full_name)
                fellow_single_allocation = {}#the dict will include person name
                #office allocated and living space allocated
                fellow_single_allocation['name'] = person.full_name
                fellow_single_allocation['office'] = self.offices['available'][
                    randint(0, (len(self.offices['available']) - 1))]
                fellow_single_allocation['living_space'] = self.living_spaces['available'][
                    randint(0, (len(self.living_spaces['available']) - 1))]
                self.fellow_allocations.append(fellow_single_allocation)
                for room in self.rooms:
                    if room.room_name == fellow_single_allocation['office']:
                        if room.capacity > 0:
                            room.capacity = room.add_person(person.full_name)
                        else:
                            self.offices['available'].remove(room.room_name)
                            self.offices['unavailable'].append(room.room_name)
                            self.unallocated_persons.append(person.full_name)
                            msg = '%s has reached its Maximum capacity.' % room.room_name
                            msg += 'Please add another %s.' % room.room_type
                            click.secho(msg, fg='red', bold=True)
                    elif room.room_name == fellow_single_allocation['living_space']:
                        if room.capacity > 0:
                            room.capacity = room.add_person(person.full_name)
                        else:
                            self.living_spaces[
                                'available'].remove(room.room_name)
                            self.living_spaces[
                                'unavailable'].append(room.room_name)
                            self.unallocated_persons.append(person.full_name)
                            msg = '%s has reached its Maximum capacity.' % room.room_name
                            msg += 'Please add another %s.' % room.room_type
                            click.secho(msg, fg='red', bold=True)
                            return click.secho('Fellow %s has been allocated Office %s'\
                                   %(person.full_name, fellow_single_allocation['office']), \
                                   fg='green')
                return click.secho('Fellow %s has been allocated office %s and living space %s'\
                                    %(person.full_name, fellow_single_allocation['office'],
                                      fellow_single_allocation['living_space']), fg='green')
                #return 'Fellow allocated both living space and office'
            else:
                if len(self.offices['available']) == 0:
                    return self.unallocated_persons.append(person.full_name)
                fellow_single_allocation = {}
                fellow_single_allocation['name'] = person.full_name
                fellow_single_allocation['office'] = self.offices['available'][
                    randint(0, (len(self.offices['available']) - 1))]
                self.fellow_allocations.append(fellow_single_allocation)
                for room in self.rooms:
                    if room.room_name == fellow_single_allocation['office']:
                        if room.capacity > 0:
                            room.capacity = room.add_person(person.full_name)
                        else:
                            self.offices['available'].remove(room.room_name)
                            self.offices['unavailable'].append(room.room_name)
                            self.unallocated_persons.append(person.full_name)
                            msg = '%s has reached its Maximum capacity.' % room.room_name
                            msg += 'Please add another %s.' % room.room_type
                            click.secho(msg, fg='red', bold=True)
                            return click.secho('Fellow %s has been allocated living space %s'\
                                   %(person.full_name, fellow_single_allocation['living_space']),\
                                    fg='green')
                return click.secho('Fellow %s has been allocated Office %s'\
                                   %(person.full_name, fellow_single_allocation['office']), \
                                   fg='green')
    def print_allocations(self, filename=None):
        """
        This prints allocations to the screen and
        highlights if they are empty or have any
        occupants, thereafter printing everyone who
        is in the particular room.
        """
        if not self.rooms:
            click.secho('THERE ARE NO ROOMS IN THE SYSTEM.',
                        fg='red', bold=True)
            return 'Error. No rooms within system.'
        msg = ''
        for room in self.rooms:
            msg += '==' * 10
            msg += '\n'
            msg += room.room_name + '(' + room.room_type + ')'
            msg += '\n'
            msg += '==' * 10
            msg += '\n'
            if room.occupants:
                for occupant in room.occupants:
                    msg += occupant
                    msg += '\n'
            else:
                msg += 'There are no people in %s yet.' % room.room_name
                msg += '\n'
        if filename is None:
            click.secho(msg, fg='cyan')
            return 'Print to screen'

        else:
            file = open(filename + '.txt', 'w')
            file.write(msg)
            click.secho('Printed to %s.txt' % filename, fg='green')
            return 'Print to file'
    def print_room(self, room_name):
        '''
        This function gets a room name as an argument and proceeds
        to display the results on the occupants of the room if any.
        '''
        if not self.rooms:
            click.secho('THERE ARE NO ROOMS IN THE SYSTEM YET.',
                        fg='red', bold=True)
            return 'No rooms exist at the moment.'
        all_rooms = []
        for room in self.rooms:
            all_rooms.append(room.room_name)
        if room_name.capitalize() not in all_rooms:
            click.secho('The room %s does not exist on our system.' %
                        room_name, fg='red', bold=True)
            return 'Room does not exist.'
        room_name = room_name.capitalize()
        for room in self.rooms:
            if room.room_name == room_name:
                click.secho('ROOM NAME:%s(%s)' %
                            (room_name, room.room_type),
                            fg='yellow', bold=True)
                click.secho('=' * 20, fg='cyan')
                if room.occupants:
                    for occupant in room.occupants:
                        click.secho(occupant, fg='yellow')
                else:
                    click.secho('Its lonely here.', fg='cyan', bold=True)
                    return False

    def print_unallocated(self, filename=None):
        '''
        After Max capacity has been recorded in a particular
        room, the person is thereafter appended to a the unallocated
        persons list.
        '''
        if not self.unallocated_persons:
            click.secho('There are no unallocated people as of now.',
                        fg='green', bold=True)
            return 'No unallocated people as per now.'
        else:
            if filename is None:
                click.secho('UNALLOCATED PEOPLE IN MY DOJO',
                            fg='red', bold=True)
                output = ''
                for unallocated in self.unallocated_persons:
                    output += unallocated
                    output += '\n'
                click.secho(output, fg='yellow')
                return 'Some people unallocated.'
            else:
                file = open(filename + '.txt', 'w')
                file.write("UNALLOCATED PEOPLE IN MY DOJO")
                file.write('\n')
                for unallocated in self.unallocated_persons:
                    file.write(unallocated)
                    file.write('\n')
                click.secho('Print out made to %s.txt' % filename, fg='green')

    def reallocate_person(self, person_id, room_name):
        '''
        The beginning of the method validates of the data passed
        is a string and then proceeds to take the person_id and
        accordingly reallocate them.
        PERSON_ID which in this case is the identifier
        is converted to upper case.
        '''
        available_rooms = []
        if not isinstance(room_name, str):
            return 'Error. Please enter valid room name.'
        for room in self.offices['available']:
            available_rooms.append(room)
        for room in self.living_spaces['available']:
            available_rooms.append(room)
        person_id = person_id.upper()
        room_name = room_name.capitalize()
        for person in self.people:
            if person.full_name in self.unallocated_persons and person.identifier == person_id:
                click.secho("Person is not allocated. Please use 'reallocate unallocated'",
                            fg='yellow', bold=True)
                return 'unallocated person.'
        if room_name.capitalize() not in available_rooms:
            click.secho('Room name %s does not exist.' %
                        room_name, fg='red', bold=True)
            return 'Room does not exist.'
        for person in self.people:
            if person.accomodate == 'N' and person.identifier == person_id:
                if room_name in self.living_spaces['available']:
                    click.secho(
                        'Cant move person from office to living space',
                        fg='red', bold=True)
                    return 'Fellow does not want accomodation'
        all_person_ids = []
        for person in self.people:
            all_person_ids.append(person.identifier)
            if person.identifier == person_id:
                person_name = person.full_name
        if person_id not in all_person_ids:
            click.secho('Person ID entered does not exist.',
                        fg='red', bold=True)
            return "Invalid person id."
        for person in self.people:
            if person.identifier == person_id:
                wanted_name = person.full_name
        for room in self.rooms:
            if wanted_name in room.occupants and \
                    room.room_name == room_name:
                click.secho('You cannot be reallocated to the same room.',
                            fg='red', bold=True)
                return 'cant reallocate to same room'
        if room_name in self.offices['available']:
            room_t = 'Office'
        if room_name in self.living_spaces['available']:
            room_t = 'Living Space'
        for room in self.rooms:
            if person_name in room.occupants and room_t == room.room_type:
                current_room = room.room_name
                room.occupants.remove(person_name)

        # Reallocate to actual room
        for room in self.rooms:
            if room.room_name == room_name and room.capacity > 0:
                room.capacity = room.add_person(person_name)
                click.secho('%s has been reallocated from %s to %s.' %
                            (person_name, current_room, room.room_name),
                            fg='green', bold=True)
                return 'Person reallocated to %s' % room_name

    def reallocate_unallocated(self, person_id, room_name):
        # Reallocate someone who is in the unallocated section
        available_rooms = []
        if not isinstance(room_name, str):
            return 'Error. Please enter valid room name.'
        room_name = room_name.capitalize()
        person_id = person_id.upper()
        people_ids = []
        for person in self.people:
            people_ids.append(person.identifier)
        if person_id not in people_ids:
            click.secho('Person ID does not exist', fg='red', bold=True)
            return 'Person ID does not exist.'

        for room in self.offices['available']:
            available_rooms.append(room)
        for room in self.living_spaces['available']:
            available_rooms.append(room)
        if room_name.capitalize() not in available_rooms:
            click.secho('Room name %s does not exist or is full.' %
                        room_name, fg='red', bold=True)
            return 'Room does not exist.'
        for person in self.people:
            if person.full_name in self.unallocated_persons and \
                    person.identifier == person_id:
                unallocated_person = person.full_name
        for room in self.rooms:
            if room.room_name == room_name:
                room.occupants.append(unallocated_person)
                self.unallocated_persons.remove(unallocated_person)
                click.secho('%s reallocated to %s' % (
                    unallocated_person, room_name), fg='green', bold=True)
