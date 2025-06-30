def solve(
    jamies_last_name_length: int = 4,  # Jamie’s last name is Grey, which has 4 letters
    letters_removed_from_bobbie: int = 2,  # Bobbie took two letters off her last name
    difference_samantha_bobbie: int = 3  # Samantha’s last name has three fewer letters than Bobbie’s
):
    """Index: 22.
    Returns: the number of letters in Samantha’s last name.
    """
    #: L1
    bobbies_last_name_length = jamies_last_name_length * 2 + letters_removed_from_bobbie # eval: 10 = 4 * 2 + 2
    #: L2
    samanthas_last_name_length = bobbies_last_name_length - difference_samantha_bobbie # eval: 7 = 10 - 3
    answer = samanthas_last_name_length  # FINAL ANSWER # eval: 7 = 7  # FINAL ANSWER
    return answer # eval: return 7