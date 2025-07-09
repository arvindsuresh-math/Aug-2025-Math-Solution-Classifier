def solve(
    jamie_last_name_len: int = 4, # Jamie Grey.
    bobbie_letters_removed: int = 2, # Bobbie took two letters off her last name
    bobbie_name_multiplier: int = 2, # she would have a last name twice the length of Jamie’s
    samantha_letters_fewer: int = 3 # Samantha’s last name has three fewer letters than Bobbie’s last name.
):
    """Index: 22.
    Returns: the number of letters in Samantha's last name.
    """

    #: L1
    bobbie_last_name_len = (bobbie_letters_removed * bobbie_name_multiplier) + bobbie_letters_removed

    #: L2
    samantha_last_name_len = bobbie_last_name_len - samantha_letters_fewer

    #: FA
    answer = samantha_last_name_len
    return answer