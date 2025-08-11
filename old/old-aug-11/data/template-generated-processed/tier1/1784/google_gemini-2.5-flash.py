def solve():
    """Index: 1784.
    Returns: the number of tortilla chips Nancy kept for herself.
    """
    # L1
    chips_given_to_brother = 7 # gives 7 tortilla chips to her brother
    chips_given_to_sister = 5 # 5 tortilla chips to her sister
    chips_given_away = chips_given_to_brother + chips_given_to_sister

    # L2
    initial_chips = 22 # a bag containing 22 tortilla chips
    chips_kept_by_nancy = initial_chips - chips_given_away

    # FA
    answer = chips_kept_by_nancy
    return answer