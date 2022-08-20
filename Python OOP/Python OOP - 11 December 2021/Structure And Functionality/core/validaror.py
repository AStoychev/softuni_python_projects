class Validator:

    @staticmethod
    def raise_if_word_is_less_than(word, min_len, message):
        if len(word) < min_len:
            raise ValueError(message)

    @staticmethod
    def raise_is_number_not_in_range(number, min_number, max_number, message):
        if number < min_number or number > max_number:
            raise ValueError(message)

    @staticmethod
    def raise_if_string_contains_empty_string_or_white_space(word, message):
        if word.strip() == "":
            raise ValueError(message)