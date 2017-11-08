import unittest
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from src.person import Staff, Fellow
from src.room import Office, LivingSpace

class TestPersonClassFunctionality(unittest.TestCase):
    '''
    This class is effectively used to manage the basics
    of how the Person class passes its properties to
    Fellow and Staff and handles how they are managed.
    '''

    def test_staff_role(self):
        s = Staff('Felicity', 'Smoke')
        self.assertEqual(s.role, 'Staff')
        # string formatting should occur as highlited above

    def test_fellow_role(self):
        s = Fellow('Elon', 'Musk')
        self.assertEqual(s.role, 'Fellow')


class TestRoomClassFunctionality(unittest.TestCase):
    """docstring for TestRoomClassFunctionality
    This Class Checks to make sure the objects created are indeed
    instances of the classes that they are instantiated from.
    It also  ensures they return values as expected.
        """

    def test_office_is_instance_of_class_Office(self):
        '''
        This simply tests that the room type and room_name are passed
        accordingly for a office. The second assert tests whether string
        formatting actually occurred
        '''
        office = Office('star_labs')
        self.assertEqual('Office', office.room_type)
        self.assertNotEqual('star_labs', office.room_name)

    def test_living_space_is_instance_of_class_LivingSpace(self):
        ls = LivingSpace('maskani')
        self.assertEqual('Living Space', ls.room_type)

    def test_capacity_of_objects(self):
        """
        The capacity of an office is set to 6
        and that of a living space is set to 4.
        This assert confirms that.
        """
        office = Office('server')
        ls = LivingSpace('bedroom')
        self.assertEqual(office.capacity, 6)
        self.assertEqual(ls.capacity, 4)

    def test_living_capacity_reduces_when_person_added(self):
        '''
        The method abstracts the room occupants indeed do
        decrease by one when the add person function is called.
        '''
        ls = LivingSpace('envy')
        self.assertEqual(ls.add_person('one'), 3)

    def test_office_capacity_reduces_when_person_added(self):
        '''
        The method here abstracts the room occupants indeed do
        decrease by one when the add person function is called.
        '''
        of = Office('starroom')
        self.assertEqual(of.add_person('one'), 5)

if __name__ == '__main__':
    unittest.main()
        
