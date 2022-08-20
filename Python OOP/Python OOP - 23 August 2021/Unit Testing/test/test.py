from unittest import TestCase, main

from project.library import Library


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library("Library")

    def test_init_functionality_with_out_property(self):
        person = Library("Name")

        self.assertEqual("Name", person.name)
        self.assertEqual({}, person.books_by_authors)
        self.assertEqual({}, person.readers)

    def test_init_functionality_with_property(self):
        with self.assertRaises(ValueError) as ex:
            person = Library("")
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_with_not_existed_author(self):
        author = "FirstAuthor"
        title = ["Book1", "Book2"]
        self.library.add_book("FirstAuthor", "Book1")
        self.library.add_book("FirstAuthor", "Book1")
        self.library.add_book("FirstAuthor", "Book2")

        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertTrue(author in self.library.books_by_authors)
        self.assertEqual(title, self.library.books_by_authors[author])

    def test_add_reader_with_not_existing_name(self):
        name = "Name"
        self.library.add_reader(name)

        self.assertEqual(1, len(self.library.readers))
        self.assertTrue(name in self.library.readers)
        self.assertEqual([], self.library.readers[name])

    def test_add_reader_with_existing_name(self):
        name = "Name"
        self.library.add_reader(name)
        result = self.library.add_reader(name)

        self.assertEqual(f"{name} is already registered in the {self.library.name} library.", result)

    def test_not_registered_person_take_rent_book(self):
        name = "Name"
        result = self.library.rent_book(name, "FirstAuthor", "Book1")

        self.assertEqual(f"{name} is not registered in the {self.library.name} Library.", result)

    def test_find_book_with_author_not_registered(self):
        name = "Name"
        author = "FirstAuthor"
        self.library.add_reader(name)

        result = self.library.rent_book(name, author, "Book1")

        self.assertEqual(f"{self.library.name} Library does not have any {author}'s books.", result)

    def test_library_have_not_author_and_book_title(self):
        name = "Name"
        author = "FirstAuthor"
        book = "Book1"
        self.library.add_reader(name)
        self.library.add_book(author, "Book3")

        result = self.library.rent_book(name, author, book)

        self.assertEqual(f"""{self.library.name} Library does not have {author}'s "{book}".""", result)

    def test_rent_book_with_name_author_and_title(self):
        name = "Name"
        author = "FirstAuthor"
        book = "Book1"
        book_1 = "Book2"
        self.library.add_reader(name)
        self.library.add_book(author, book)
        self.library.add_book(author, book_1)

        result = self.library.rent_book(name, author, book)
        self.assertEqual([{author: book}], self.library.readers[name])
        self.assertTrue(book not in self.library.books_by_authors[author])
        self.assertTrue(book_1 in self.library.books_by_authors[author])
        self.assertEqual(1, len(self.library.books_by_authors[author]))


if __name__ == "__main__":
    main()