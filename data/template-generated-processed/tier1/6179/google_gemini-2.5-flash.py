def solve():
    """Index: 6179.
    Returns: the predicted age Sarah will get married.
    """
    # L1
    sarah_name_letters = 5 # Sarah's name has 5 letters
    letters_in_name = sarah_name_letters

    # L2
    multiplier_for_twice = 2 # WK
    sarah_age = 9 # Sarah is 9 years old
    twice_sarah_age = multiplier_for_twice * sarah_age

    # L3
    predicted_marriage_age = letters_in_name + twice_sarah_age

    # FA
    answer = predicted_marriage_age
    return answer