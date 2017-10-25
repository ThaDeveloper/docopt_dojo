import unittest
from dojo import Dojo

class TestCreateRoom(unittest.TestCase):
    def test_create_room_successfully(self):
        room = Room()
        initial_room_count = len(room.all_rooms)
        finance = room.create_room("finance", "office")
        self.assertTrue(finance)
        new_room_count = len(room.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

        
class TestAddPerson(unittest.TestCase):
    def test_add_person_successfully(self):
        person = Person()
        initial_person_count = len(person.all_persons)
        justin = person.add_person("justin", "fellow")
        self.assertTrue(justin)
        new_person_count = len(person.all_persons)
        self.assertEqual(new_person_count - initial_person_count, 1)
if __name__ == '__main__':
    unittest.main()