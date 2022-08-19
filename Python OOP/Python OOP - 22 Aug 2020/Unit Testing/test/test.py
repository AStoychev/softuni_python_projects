from unittest import TestCase, main
from project.student_report_card import StudentReportCard


class TestStudentReport(TestCase):
    def setUp(self) -> None:
        self.card = StudentReportCard("Name", 5)

    def test_init_is_correctly(self):
        self.assertEqual("Name", self.card.student_name)
        self.assertEqual(5, self.card.school_year)
        self.assertEqual({}, self.card.grades_by_subject)

    def test_property_for_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.card.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_property_for_school_year_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.card.school_year = 30
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_property_for_school_year_is_less_than_zero_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.card.school_year = -1
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_add_grade_without_existing_subject(self):
        subject = "english"
        self.card.add_grade(subject, 5.50)
        self.assertTrue(subject in self.card.grades_by_subject)
        self.assertEqual([5.50], self.card.grades_by_subject[subject])

    def test_add_grade_with_existing_subject(self):
        subject = "english"
        self.card.add_grade(subject, 5.50)
        self.card.add_grade(subject, 6)
        self.assertEqual([5.50, 6], self.card.grades_by_subject[subject])
        self.assertTrue(5.50, 6 in self.card.grades_by_subject[subject])
        self.assertEqual(2, len(self.card.grades_by_subject[subject]))

    def test_average_grade_by_subject(self):
        subject = "english"
        self.card.add_grade(subject, 5.50)
        self.card.add_grade(subject, 6)
        second_subject = "mathematics"
        self.card.add_grade(second_subject, 5.35)
        self.card.add_grade(second_subject, 5.12)

        result = self.card.average_grade_by_subject()
        self.assertEqual(f"{subject}: 5.75\n{second_subject}: 5.23", result)

    def test_average_grades_by_all_subject(self):
        subject = "english"
        self.card.add_grade(subject, 5.50)
        self.card.add_grade(subject, 6)
        second_subject = "mathematics"
        self.card.add_grade(second_subject, 5.35)
        self.card.add_grade(second_subject, 5.12)

        result = self.card.average_grade_for_all_subjects()
        self.assertEqual("Average Grade: 5.49", result)

    def test_repr_is_correctly(self):
        subject = "english"
        self.card.add_grade(subject, 5.50)
        self.card.add_grade(subject, 6)
        second_subject = "mathematics"
        self.card.add_grade(second_subject, 5.35)
        self.card.add_grade(second_subject, 5.12)

        result = self.card.__repr__()

        final_result = f"Name: {self.card.student_name}\n" \
                       f"Year: {self.card.school_year}\n" \
                       f"----------\n" \
                       f"english: 5.75\n" \
                       f"mathematics: 5.23\n" \
                       f"----------\n" \
                       f"Average Grade: 5.49"

        self.assertEqual(final_result, result)


if __name__ == "__main__":
    main()