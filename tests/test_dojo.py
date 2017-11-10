import unittest
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from dojo import Dojo


class TestDojoFunctionality(unittest.TestCase):
    '''
    The self.dojo Class here is used to hold the main functionality
    of the self.dojo Room Allocation system. It imports and makes calls
    to all other classes and manages them to create necessary instances
    and performs the necessary logic. This Test Class thus tests
    all the logic approporately.
    '''

    def setUp(self):
        self.dojo = Dojo()

    def test_dojo_class_initialises_with_nothing(self):
        self.assertEquals(len(self.dojo.rooms), 0)
        self.assertEquals(len(self.dojo.people), 0)
        self.assertEquals(len(self.dojo.fellows), 0)
        self.assertEquals(len(self.dojo.staff), 0)

    # create room method test functionality begins here
    def test_returns_error_when_non_string_is_addded(self):
        self.assertEqual(self.dojo.create_room(
            0, 2), 'Error. Invalid room type initial.',
            msg='Room name and initial must only be strings.')
        self.assertEqual(self.dojo.create_room('w', 'WorkSpace'),
                         'Error. Invalid room type initial.',
                         msg='Enter O or L for room type inital.')

    def test_create_room_method(self):
       self.dojo.create_room("o", "hr")
       self.assertIn("Hr", self.dojo.offices['available'])
       self.dojo.create_room('l', 'hood')
       self.assertIn('Hood', self.dojo.living_spaces['available'])

    def test_create_room_adds_one_to_list(self):
        room_count_before = len(self.dojo.rooms)
        self.dojo.create_room("o", "hr")
        room_count_after = len(self.dojo.rooms)
        self.assertEquals((room_count_after - room_count_before), 1)
           

    def test_living_space_can_only_be_created_once(self):
        self.dojo.create_room('l', 'dungeon')
        result = self.dojo.create_room('l', 'dungeon')
        self.assertEqual(result, 'Room already exists.')

    def test_office_can_only_be_created_once(self):
        self.dojo.create_room('o', 'board')
        result = self.dojo.create_room('o', 'board')
        self.assertEqual(result, 'Room already exists.')

    def test_room_creation_when_successful(self):
        result = self.dojo.create_room('o', 'server')
        self.assertEqual(result, 'Room Server created.')
        result = self.dojo.create_room('l', 'oracle')
        self.assertEqual(result, 'Room Oracle created.')

    # Print allocations method test begins here
    def test_returns_no_allocations_if_no_rooms_created(self):
        self.assertEqual(self.dojo.print_allocations(),
                         'Error. No rooms within system.')
    # add_person method testing begins here

    def test_returns_error_if_no_rooms_within_system(self):
        result = self.dojo.validate_person('Black', 'Canary', 'Fellow', 'Y')
        self.assertEqual(result, 'There are no rooms in the system.')

    def test_validation_of_people_names(self):
        self.dojo.create_room('o', 'hr')
        res = self.dojo.validate_person('Black', 24, 'Fellow', 'y')
        self.assertTrue(res)
        self.assertEqual(res, 'Wrong type for name.')
        res2 = self.dojo.validate_person('KH233vc', 'Canary', 'Fellow', 'Y')
        self.assertTrue(res2)
        self.assertEqual(res2, 'Non-Alphabetical names added')

    def test_validation_of_people_types(self):
        self.dojo.create_room('o', 'spacex')
        res = self.dojo.validate_person('Elon', 'Musk', 'worker', 'y')
        self.assertTrue(res)
        self.assertEqual(res, 'Invalid role')

    def test_wants_accomodation_is_either_y_or_n(self):
        self.dojo.create_room('o', 'meeting')
        res = self.dojo.validate_person(
            'Tracy', 'Kaloki', 'Fellow', 'No')
        self.assertTrue(res)
        self.assertEqual(res, 'Wants accomodation not Y or N')

    def test_validation_if_person_fellow_and_wants_accomodation(self):
        '''
        Both a living space and office must exist for a fellow who
        wants accomodation.
        '''
        self.dojo.create_room('o', 'hr')
        res = self.dojo.validate_person('Lebron', 'James', 'Fellow', 'Y')
        self.assertTrue(res)
        self.assertEqual(res, 'No Living space for fellow requiring both.')

    def test_passes_validation_and_creates_person(self):
        # Since there are only two rooms: one of each Living Space and Office
        # and person wants accomodation
        # we are sure the rooms allocated are as created.
        self.dojo.create_room('o', 'cavaliers')
        self.dojo.create_room('l', 'oracle')
        res = self.dojo.validate_person('isaiah', 'thomas', 'Fellow', 'y')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        for room in self.dojo.rooms:
            if room.room_name == 'cavaliers':
                self.assertIn('Isaiah Thomas', room.occupants)
                self.assertEqual(len(room.occupants), 1)
            if room.room_name == 'oracle':
                self.assertIn('Isaiah Thomas', room.occupants)
                self.assertEqual(len(room.occupants), 1)

    def test_person_objects_are_created(self):
        self.dojo.create_room('o', 'nba')
        self.dojo.create_room('l', 'nfl')
        res = self.dojo.validate_person('talib', 'kweli', 'Fellow', 'y')
        person = self.dojo.generate_identifier(res)
        for person in self.dojo.people:
            if person.full_name == 'Talib Kweli':
                self.assertEqual(person.role, 'Fellow')
                self.assertEqual(person.identifier, 'F1')

        res2 = self.dojo.validate_person('giannis', 'antetokounmpo', 'Staff', 'n')
        person = self.dojo.generate_identifier(res2)
        for person in self.dojo.people:
            if person.full_name == 'Giannis Aantekokuompo':
                self.assertEqual(person.role, 'Staff')
                self.assertEqual(person.identifier, 'S1')

    def test_get_identifier_if_no_people_added(self):
        self.assertEqual(self.dojo.get_identifier(
            'Lili', 'Scott'), 'No people added')

    def test_get_identifier_if_people_added(self):
        self.dojo.create_room('o', 'audi')
        self.dojo.create_room('l', 'lexus')
        res = self.dojo.validate_person('mr', 'miyagi', 'Fellow', 'y')
        res = self.dojo.generate_identifier(res)
        self.assertEqual(self.dojo.get_identifier(
            'mr', 'miyagi'), 'F1')
    # Test Reallocate Person starts here

    def test_reallocate_person(self):
        self.dojo.create_room('o', 'bmw')
        self.dojo.create_room('o', 'subaru')
        res = self.dojo.validate_person('dodge', 'challenger', 'staff', 'n')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        res = self.dojo.reallocate_person('S1', [])
        self.assertEqual(res, "Error. Please enter valid room name.")

    def test_reallocate_person_when_room_does_not_exist(self):
        self.dojo.create_room('o', 'kenya')
        self.dojo.create_room('o', 'uganda')
        res = self.dojo.validate_person('Shy', 'Girl', 'staff', 'n')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        res = self.dojo.reallocate_person('S1', 'Tanzania')
        self.assertEqual(res, "Room does not exist.")

    def test_reallocate_person_when_person_accomodate_is_N(self):
        self.dojo.create_room('o', 'Kenya')
        self.dojo.create_room('l', 'Uganda')
        res = self.dojo.validate_person('John', 'Diggle', 'Fellow', 'n')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        res = self.dojo.reallocate_person('F1', 'Uganda')
        self.assertEqual(res, 'Fellow does not want accomodation')
        for room in self.dojo.rooms:
            if room.room_name == 'Uganda':
                self.assertNotIn('John Diggle', room.occupants)

    def test_reallocate_to_same_room(self):
        self.dojo.create_room('o', 'Kenya')
        res = self.dojo.validate_person('Missy', 'Elliot', 'Fellow', 'n')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        res = self.dojo.reallocate_person('F1', 'Kenya')
        self.assertEqual(res, 'cant reallocate to same room')

    def test_reallocate_to_same_room_if_person_id_non_exitent(self):
        self.dojo.create_room('o', 'Kenya')
        self.dojo.create_room('o', 'Uganda')
        res = self.dojo.validate_person(
            'Missy', 'Elliot', 'Staff', 'n')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        res = self.dojo.reallocate_person('Staff1', 'Kenya')
        self.assertEqual(res, 'Invalid person id.')

    def test_reallocate_person_works(self):
        self.dojo.create_room('o', 'dungeo')
        res = self.dojo.validate_person(
            'Missy', 'Elliot', 'Staff', 'n')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        self.dojo.create_room('o', 'palace')
        res = self.dojo.reallocate_person('S1', 'palace')
        self.assertEqual(res, 'Person reallocated to Palace')
        for room in self.dojo.rooms:
            if room.room_name == 'dungeon':
                self.assertNotIn('Missy Elliot', room.occupants)
            if room.room_name == 'Dungeon':
                self.assertIn('Missy Elliot', room.occupants)

    def test_reallocate_unallocated(self):
        self.dojo.create_room('o', 'lab')
        res = self.dojo.validate_person('Albert', 'Einsten', 'staff')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        res = self.dojo.reallocate_unallocated('s222', 'Lab')
        self.assertEqual(res, 'Person ID does not exist.')
    # test_print_room_works

    def test_print_room_if_no_rooms(self):
        res = self.dojo.print_room('canada')
        self.assertEqual(res, 'No rooms exist at the moment.')

    def test_if_room_exists(self):
        self.dojo.create_room('o', 'canada')
        res = self.dojo.print_room('NOTROOM')
        self.assertEqual(res, 'Room does not exist.')

    # test print unallocated
    def test_print_unallocated_if_all_allocated(self):
        self.dojo.create_room('o', 'science')
        res = self.dojo.validate_person('Nikola', 'Tesla', 'Staff', 'n')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        res = self.dojo.print_unallocated()
        self.assertEqual(res, 'No unallocated people as per now.')

    def test_print_unallocated_if_exisiting(self):
        self.dojo.create_room('o', 'Tesla')
        res = self.dojo.validate_person('Nikola', 'Tesla', 'Staff', 'n')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        self.dojo.unallocated_persons.append('Person Name')
        res = self.dojo.print_unallocated()
        self.assertTrue(res, 'Some people unallocated.')
    # save state functionality

    '''   def test_save_state(self):
        self.dojo.create_room('o', 'Tesla')
        res = self.dojo.validate_person('Nikola', 'Tesla', 'Staff', 'n')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        self.assertFalse(os.path.exists('default_db_self.dojo.sqlite'))

    def save_state_works(self):
        self.dojo.create_room('o', 'Tesla')
        res = self.dojo.validate_person('Nikola', 'Tesla', 'Staff', 'n')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        res = self.dojo.save_state()
        self.assertEqual(res, True) '''

    # additional tests
    def test_returns_correct_message(self):
        self.dojo.create_room('o', 'mordor')
        res = self.dojo.validate_person(
            'Gandalf', 'Gray', 'Staff', 'n')
        person = self.dojo.generate_identifier(res)
        self.dojo.allocate_room(person)
        res = self.dojo.print_allocations()
        self.assertEqual(res, 'Print to screen')
        res2 = self.dojo.print_allocations('test_dandalf')
        self.assertEqual(res2, 'Print to file')

    '''  # test database loaded
    def test_database_loaded(self):
        self.dojo.create_room('o', 'mordor')
        self.dojo.create_room('l', 'shire')
        self.dojo.save_state()
        res = self.dojo.load_state('default_dojo_db')
        self.assertEqual(res, 'Database Loaded.') '''
    
if __name__ == '__main__':
    unittest.main()