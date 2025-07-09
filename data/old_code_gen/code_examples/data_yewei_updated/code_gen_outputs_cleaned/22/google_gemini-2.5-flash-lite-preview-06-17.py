def solve(
    jamie_last_name_letters: int = 4, # Jamie Grey.
    bobbie_letters_removed: int = 2, # Bobbie took two letters off her last name
    samantha_letters_fewer: int = 3 # Samantha’s last name has three fewer letters than Bobbie’s last name.
):
    """Index: 22.
    Returns: the number of letters in Samantha's last name.
    """
    #: L1
    bobbie_last_name_letters = (jamie_last_name_letters * 2) + bobbie_letters_removed

    #: L2
    samantha_last_name_letters = bobbie_last_name_letters - samantha_letters_fewer

    answer = samantha_last_name_letters # FINAL ANSWER
    return answer