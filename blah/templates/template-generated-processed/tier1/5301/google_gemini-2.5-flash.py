def solve():
    """Index: 5301.
    Returns: the number of lines the first character has.
    """
    # L1
    third_character_lines = 2 # The third character only has two lines
    multiplier_for_third_char = 3 # three times the number of lines the third character has
    additional_lines_for_second_char = 6 # six more than three times
    product_of_multiplier_and_third = multiplier_for_third_char * third_character_lines
    second_character_lines = additional_lines_for_second_char + product_of_multiplier_and_third

    # L2
    first_char_more_than_second = 8 # eight more lines than the second character
    first_character_lines = second_character_lines + first_char_more_than_second

    # FA
    answer = first_character_lines
    return answer