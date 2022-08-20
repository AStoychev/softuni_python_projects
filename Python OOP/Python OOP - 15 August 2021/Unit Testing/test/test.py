from unittest import TestCase, main
from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("Name")

    def test_init_is_work_correctly(self):
        self.assertEqual("Name", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_if_food_is_less_than_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food("Food", -1)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_add_food_if_food_is_equal_to_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food("Food", 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_add_food_if_name_not_in_food(self):
        self.shop.add_food("Food", 50)
        self.assertEqual(50, self.shop.food["Food"])
        self.assertTrue("Food" in self.shop.food)
        self.assertEqual(1, len(self.shop.food))

    def test_add_food_if_name_exist_in_food(self):
        self.shop.food["Food"] = 50
        result = self.shop.add_food("Food", 30)
        self.assertEqual("Successfully added 30.00 grams of Food.", result)
        self.assertTrue("Food" in self.shop.food)
        self.assertEqual(80, self.shop.food["Food"])

    def test_add_pet_if_pet_not_exist_in_list(self):
        result = self.shop.add_pet("Vasko")
        self.assertEqual("Successfully added Vasko.", result)
        self.assertTrue("Vasko" in self.shop.pets)
        self.assertEqual(1, len(self.shop.pets))

    def test_add_pet_if_pet_exist_in_list(self):
        self.shop.add_pet("Vasko")
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Vasko")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_if_current_pet_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("Food", "Vasko")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_if_food_not_exist(self):
        self.shop.add_pet("Vasko")
        result = self.shop.feed_pet("Food", "Vasko")
        self.assertEqual("You do not have Food", result)

    def test_feed_pet_if_food_is_a_little_in_list(self):
        self.shop.add_pet("Vasko")
        self.shop.food["Food"] = 50
        result = self.shop.feed_pet("Food", "Vasko")
        self.assertEqual("Adding food...", result)
        self.assertTrue("Food" in self.shop.food)
        self.assertEqual(1050, self.shop.food["Food"])

    def test_feed_pet_if_all_in_list(self):
        self.shop.add_pet("Vasko")
        self.shop.food["Food"] = 1100
        result = self.shop.feed_pet("Food", "Vasko")
        self.assertEqual("Vasko was successfully fed", result)
        self.assertTrue("Vasko" in self.shop.pets)
        self.assertEqual(1000, self.shop.food["Food"])

    def test_repr_is_correctly(self):
        self.shop.add_pet("Vasko")
        self.shop.add_pet("Vasko1")
        self.shop.add_pet("Vasko3")

        result = self.shop.__repr__()

        self.assertEqual(f"Shop Name:\nPets: Vasko, Vasko1, Vasko3", result)










if __name__ == "__main__":
    main()