import unittest
from dojo import Dojo


class TestAddPerson(unittest.TestCase):
    def test_add_person_successfully(self):
        person = Person()
        initial_person_count = len(person.all_persons)
        justin = person.add_person("justin", "fellow")
        self.assertTrue(justin)
        new_person_count = len(person.all_persons)
        self.assertEqual(new_person_count - initial_person_count, 1)

    def test_person_role(self):
        person = Person()
        justin = person.add_person("justin", "staff")
        self.assertEqual("justin", justin)

class TestCreateRoom(unittest.TestCase):
    def test_create_room_successfully(self):
        room = Room()
        initial_room_count = len(room.all_rooms)
        finance = room.create_room("finance", "office space")
        self.assertTrue(finance)
        new_room_count = len(room.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_room_type(self):
        room = Room()
        the hood = room.create_room("the hood", "living space")
        self.assertEqual("the hood", the hood)
class TestDojoAllocation(unittest.TestCase):
    def test_room_required(self):
        person = Person()
        justin = person.add_person("justin", "fellow")
        opt = person.living_opt(justin, 1)
        self.assertEqual(justin.find_room(justin,opt), ["office", "living space"])

if __name__ == '__main__':
    unittest.main()
        
