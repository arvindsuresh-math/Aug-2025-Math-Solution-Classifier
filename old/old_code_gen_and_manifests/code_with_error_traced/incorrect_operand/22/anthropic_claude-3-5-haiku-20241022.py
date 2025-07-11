def solve(
    jamie_last_name: str = "Grey", # Jamie's full name is Jamie Grey
    letters_difference: int = 3 # Samantha's last name has three fewer letters than Bobbie's
):
    """Index: 22.
    Returns: the number of letters in Samantha's last name."""

    #: L1
    jamie_last_name_length = len(jamie_last_name) # eval: 4 = len(Grey)
    bobbie_last_name_length = jamie_last_name_length * 2 + 2 # eval: 10 = 4 * 2 + 2

    #: L2
    samantha_last_name_length = letters_difference - letters_difference # eval: 0 = 3 - 3

    #: FA
    answer = samantha_last_name_length
    return answer # eval: return 0
