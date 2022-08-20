from unittest import TestCase, main
from project.train.train import Train


class TestTrain(TestCase):

    def setUp(self) -> None:
        self.train = Train("Name", 100)

    def test_init_is_correctly(self):
        self.assertEqual("Name", self.train.name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_if_capacity_is_full(self):
        self.train.capacity = 3
        self.train.add("Vasko1")
        self.train.add("Vasko2")
        self.train.add("Vasko3")
        with self.assertRaises(ValueError) as ex:
            self.train.add("Vasko")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_passenger_if_current_name_exist_in_train(self):
        self.train.add("Vasko")
        with self.assertRaises(ValueError) as ex:
            self.train.add("Vasko")
        self.assertEqual("Passenger Vasko Exists", str(ex.exception))

    def test_add_passenger_in_train(self):
        result = self.train.add("Vasko")
        self.assertEqual("Added passenger Vasko", result)
        self.assertTrue("Vasko" in self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))

    def test_remove_passengers_if_passenger_not_exist_in_train(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Vasko")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_passenger_work_correctly(self):
        self.train.add("Vasko")
        result = self.train.remove("Vasko")
        self.assertEqual("Removed Vasko", result)