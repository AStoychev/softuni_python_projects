class Validator:
    @staticmethod
    def raise_value_error_if_string_is_empty_ot_white_space(value, message):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_value_error_if_value_is_equal_or_less_than_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_not_in_range(number, min_number, max_number, message):
        if number < min_number or number > max_number:
            raise ValueError(message)