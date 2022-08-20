from unittest import TestCase, main

from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("Name")

    def test_init(self):
        team = Team("Name")

        self.assertEqual("Name", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_if_contain_digit(self):
        with self.assertRaises(ValueError) as ex:
            team = Team("Name121241121")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member_in_name_not_in_members(self):
        self.team.members["ivan"] = 18

        result = self.team.add_member(ivan=18, gosho=21, pesho=30, vasko=30)
        self.assertEqual(f"Successfully added: gosho, pesho, vasko", result)
        self.assertEqual(18, self.team.members["ivan"])
        self.assertEqual(18, self.team.members["ivan"])
        self.assertEqual(21, self.team.members["gosho"])
        self.assertEqual(30, self.team.members["vasko"])

    def test_remove_members_with_name_who_exist_in_members(self):
        self.team.members["vasko"] = 18
        result = self.team.remove_member("vasko")
        self.assertEqual("Member vasko removed", result)
        self.assertTrue("vasko" not in self.team.members)
        self.assertEqual(0, len(self.team.members))

    def test_remove_members_with_name_who_not_in_members(self):
        result = self.team.remove_member("vasko")
        self.assertEqual("Member with name vasko does not exist", result)
        self.assertTrue("vasko" not in self.team.members)
        self.assertEqual(0, len(self.team.members))

    def test_gt_compare_team(self):
        self.team.members["vasko"] = 18
        self.team.members["vasko1"] = 30

        another_team = Team("Another")
        another_team.members["members"] = 31
        another_team.members["members1"] = 35
        another_team.members["members15"] = 38

        self.assertEqual(True, another_team > self.team)
        self.assertEqual(False, self.team > another_team)

    def test_len(self):
        self.team.members["vasko"] = 18
        self.team.members["vasko1"] = 30

        self.assertEqual(2, len(self.team))

    def test_add_new_name_in_team_members(self):
        self.team.members["vasko"] = 18
        self.team.members["vasko1"] = 30

        another_team = Team("Another")
        another_team.members["members"] = 31
        another_team.members["members1"] = 35
        another_team.members["members15"] = 38

        result = self.team + another_team

        expected_result = {
            "vasko": 18,
            "vasko1": 30,
            "members": 31,
            "members1": 35,
            "members15": 38
        }

        self.assertEqual("NameAnother", result.name)
        self.assertEqual(expected_result, result.members)

    def test_str_is_correctly(self):
        self.team.members["vasko"] = 18
        self.team.members["vasko1"] = 30

        result = f"Team name: Name\nMember: vasko1 - 30-years old\nMember: vasko - 18-years old"

        self.assertEqual(result, self.team.__str__())

        
if __name__ == "__main__":
    main()