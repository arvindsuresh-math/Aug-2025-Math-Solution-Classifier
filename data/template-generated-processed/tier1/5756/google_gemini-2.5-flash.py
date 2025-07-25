def solve():
    """Index: 5756.
    Returns: the total number of letters Jacob and Nathan can write together in 10 hours.
    """
    # L1
    nathan_letters_per_hour = 25 # Nathan wrote 25 letters in one hour
    jacob_speed_multiplier = 2 # Jacob can write twice as fast as Nathan
    jacob_letters_per_hour = nathan_letters_per_hour * jacob_speed_multiplier

    # L2
    combined_letters_per_hour = jacob_letters_per_hour + nathan_letters_per_hour

    # L3
    total_hours = 10 # in 10 hours
    total_letters = combined_letters_per_hour * total_hours

    # FA
    answer = total_letters
    return answer