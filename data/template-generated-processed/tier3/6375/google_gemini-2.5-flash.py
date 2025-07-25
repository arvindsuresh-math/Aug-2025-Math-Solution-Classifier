def solve():
    """Index: 6375.
    Returns: the total number of characters in Pat's computer password.
    """
    # L1
    first_string_length = 8 # eight random lowercase letters
    half_divisor = 2 # half that length
    second_string_length = first_string_length / half_divisor

    # L2
    symbols_per_end = 1 # one symbol on each end
    number_of_ends = 2 # WK
    total_symbol_characters = symbols_per_end * number_of_ends

    # L3
    total_password_length = first_string_length + second_string_length + total_symbol_characters

    # FA
    answer = total_password_length
    return answer