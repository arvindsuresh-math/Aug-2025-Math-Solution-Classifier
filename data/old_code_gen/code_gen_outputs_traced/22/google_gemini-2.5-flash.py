def solve(
        samantha_fewer_letters: int = 3, # three fewer letters
        bobbie_letters_off: int = 2, # two letters off her last name
        bobbie_length_multiplier: int = 2, # twice the length
        jamie_last_name_length: int = 4 # Jamie’s full name is Jamie Grey (Grey has 4 letters)
    ):
    """Index: 22.
    Returns: the number of letters in Samantha's last name.
    """

    #: L1
    bobbie_last_name_length = jamie_last_name_length * bobbie_length_multiplier + bobbie_letters_off # eval: 10 = 4 * 2 + 2

    #: L2
    samantha_last_name_length = bobbie_last_name_length - samantha_fewer_letters # eval: 7 = 10 - 3

    #: FA
    answer = samantha_last_name_length
    return answer # eval: return 7
