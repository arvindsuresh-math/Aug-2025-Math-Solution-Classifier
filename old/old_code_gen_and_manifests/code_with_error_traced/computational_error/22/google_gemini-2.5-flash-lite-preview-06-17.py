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
    bobbie_last_name_len = (jamie_last_name_len * bobbie_name_multiplier) + bobbie_letters_removed # eval: 10 = (4 * 2) + 2

    #: L2
    samantha_last_name_len = 8 # eval: 8 = 8

    #: FA
    answer = samantha_last_name_len
    return answer # eval: return 8
