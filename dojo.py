import os
import time
import click
from random import randint
from src.room import LivingSpace, Office
from src.person import Fellow, Staff
from db.models import People, Rooms, DatabaseManager, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
        if type(room_type) != str or room_type.upper() not in ['O', 'L']:
            click.secho('Error.Please enter O or L for a room type.',
                        bold=True, fg='red')
            return 'Error. Invalid room type initial.'
        room_type = room_type.strip().upper()
        room_name = room_name.strip().title()
        if room_type == 'O':
            room_type = 'Office'
        if room_type == 'L':
            room_type = 'Living Space'
        for room in self.rooms:
            if room.room_name == room_name and \
                    room.room_type == room_type:
                click.secho('%s --> %s ALREADY EXISTS.Please pick another name.'
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
        click.secho('The %s ---> %s has been created.' %
                    (room.room_type, room.room_name), bold=True, fg='green')
        return 'Room %s created.' % room.room_name
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
            # print(room.room_name)
            # print(room.occupants)
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

    def validate_person(self, first_name, other_name, person_type,
                        accomodate='N'):
        if type(first_name) != str or type(other_name) != str:
            click.secho('Incorrect name type format.', fg='red')
            return 'Wrong type for name.'
        if not first_name.isalpha() or not other_name.isalpha():
            click.secho('Person names need be alphabetical in nature',
                        fg='red', bold=True)
            return 'Non-Alphabetical names added'
        if person_type.title() not in ['Fellow', 'Staff']:
            click.secho('Please enter either Fellow or Staff for person type',
                        fg='red', bold=True)
            return 'Invalid Person Type'
        if accomodate.upper() not in ['Y', 'N']:
            click.secho('Please enter Y or N for wants accomodation.',
                        fg='red', bold=True)
            return 'Wants accomodation not Y or N'
        accomodate = accomodate.upper()
        person_type = person_type.title()
        if person_type == 'Staff' and accomodate == 'Y':
            accomodate = 'N'
            click.secho(
                'A Staff member cannot be allocated accomodation. An office will however be allocated.',
                fg='red', bold=True)
        fn = first_name.title() + ' ' + other_name.title()
        for person in self.people:
            if person.full_name == fn and \
                    person.person_type == person_type.title():
                click.secho('%s %s ALREADY EXISTS.' % (person_type, fn))
                return 'Person exists.'
        if not self.offices['available'] and person_type == 'Staff':
            click.secho(
                'There are no offices or the offices are all full.',
                fg='red', bold=True)
            return 'There are no offices in the system.'
        if not self.living_spaces['available'] and not \
                self.offices['available']:
            click.secho(
                'THERE ARE NO ROOMS IN THE SYSTEM YET OR ALL ROOMS ARE FULL.',
                fg='red', bold=True)
            return 'There are no rooms in the system.'

        if accomodate == 'Y' and person_type == 'Fellow':
            if not self.living_spaces['available']:
                msg = 'Please add a living space for a fellow '
                msg += 'to be allocated both room types.'
                click.secho(msg, fg='red', bold=True)
                return 'No Living space for fellow requiring both.'
            elif not self.offices['available']:
                msg = 'Please add an office for a fellow '
                msg += 'to be allocated both room types.'
                click.secho(msg, fg='red', bold=True)
                return 'No office for fellow requiring both.'
        return [fn, accomodate, person_type]

    def generate_identifier(self, validated_details):
        fn = validated_details[0]
        accomodate = validated_details[1]
        person_type = validated_details[2]
        full_names = fn.split()
        if not self.people:
            if person_type.title() == 'Fellow':
                f_id = 1
                self.f_ids.append(f_id)
                identifier = 'F' + str(f_id)
                person = Fellow(full_names[0], full_names[1])
                person.accomodate = accomodate
                person.get_full_name()
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
            elif person_type.title() == 'Staff':
                s_id = 1
                self.s_ids.append(s_id)
                identifier = 'S' + str(s_id)
                person = Staff(full_names[0], full_names[1])
                person.accomodate = accomodate
                person.get_full_name()
                person.assign_identifier(identifier)
                self.staff.append(person.full_name)
        else:
            if person_type.title() == 'Fellow':
                person = Fellow(full_names[0], full_names[1])
                person.accomodate = accomodate
                person.get_full_name()
                f_id = self.f_ids.pop() + 1
                identifier = 'F' + str(f_id)
                self.f_ids.append(f_id)
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
            elif person_type.title() == 'Staff':
                person = Staff(full_names[0], full_names[1])
                person.accomodate = accomodate
                person.get_full_name()
                s_id = self.s_ids.pop() + 1
                identifier = 'S' + str(s_id)
                self.s_ids.append(s_id)
                person.assign_identifier(identifier)
                self.fellows.append(person.full_name)
        self.people.append(person)
        click.secho('The %s %s has been created.\n' %
                    (person.person_type, person.full_name),
                    fg='green', bold=True)
        return person

    def allocate_room(self, person):
        # random allocation
        # only a fellow can be allocated a living space
        # a staff can only be allocated an office.
        click.secho('ALLOCATING ROOM ...', fg='cyan')
        time.sleep(1)
        if person.person_type == 'Staff':
            staff_single_allocation = {}
            staff_single_allocation[person.full_name] = self.offices['available'][
                randint(0, (len(self.offices['available']) - 1))]
            self.staff_allocations.append(staff_single_allocation)
            for room in self.rooms:
                if room.room_name == staff_single_allocation[person.full_name]:
                    if room.capacity > 0:
                        click.secho('Success!', fg='green')
                        room.capacity = room.add_person(person.full_name)
                    else:
                        self.offices['available'].remove(room.room_name)
                        self.offices['unavailable'].append(room.room_name)
                        self.unallocated_persons.append(person.full_name)
                        msg = '%s has reached its Maximum capacity.' % room.room_name
                        msg += 'Please add another %s.' % room.room_type
                        click.secho(msg, fg='red', bold=True)

        if person.person_type == 'Fellow':
            if person.accomodate == 'Y':
                fellow_single_allocation = {}
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
                click.secho('Success!', fg='green')
                return 'Fellow allocated both living space and office'
            else:
                fellow_single_allocation = {}
                fellow_single_allocation[person.full_name] = \
                    self.offices['available'][
                    randint(0, (len(self.offices['available']) - 1))]
                self.fellow_allocations.append(fellow_single_allocation)
                for room in self.rooms:
                    if room.room_name == \
                            fellow_single_allocation[person.full_name]:
                        if room.capacity > 0:
                            click.secho('Success!', fg='green')
                            room.capacity = room.add_person(person.full_name)
                        else:
                            self.offices['available'].remove(room.room_name)
                            self.offices['unavailable'].append(room.room_name)
                            self.unallocated_persons.append(person.full_name)
                            msg = '%s has reached its Maximum capacity.' % room.room_name
                            msg += 'Please add another %s.' % room.room_type
                            click.secho(msg, fg='red', bold=True)

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