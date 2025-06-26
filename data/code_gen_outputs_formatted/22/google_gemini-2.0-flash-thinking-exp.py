def solve(
    samantha_fewer_than_bobbie: int = 3, # three fewer letters than Bobbie’s last name
    bobbie_letters_removed: int = 2, # Bobbie took two letters off her last name
    bobbie_multiplier_of_jamie: int = 2, # she would have a last name twice the length of Jamie’s
    jamie_last_name_length: int = 4 # Jamie’s full name is Jamie Grey (Grey has 4 letters)
):
    """Index: 22.
    Returns: the number of letters in Samantha's last name.
    """

    #: L1
    bobbie_last_name_length = jamie_last_name_length * bobbie_multiplier_of_jamie + bobbie_letters_removed

    #: L2
    samantha_last_name_length = bobbie_last_name_length - samantha_fewer_than_bobbie

    answer = samantha_last_name_length # FINAL ANSWER
    return answer