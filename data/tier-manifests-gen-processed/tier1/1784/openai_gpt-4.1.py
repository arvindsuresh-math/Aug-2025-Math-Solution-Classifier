def solve():
    """Index: 1784.
    Returns: the number of tortilla chips Nancy kept for herself.
    """
    # L1
    chips_to_brother = 7 # gives 7 tortilla chips to her brother
    chips_to_sister = 5 # gives 5 tortilla chips to her sister
    total_given_away = chips_to_brother + chips_to_sister

    # L2
    total_chips = 22 # bag containing 22 tortilla chips
    nancy_kept = total_chips - total_given_away

    # FA
    answer = nancy_kept
    return answer