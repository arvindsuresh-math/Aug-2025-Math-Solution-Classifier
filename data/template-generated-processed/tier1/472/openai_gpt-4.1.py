def solve():
    """Index: 472.
    Returns: Lydia's age when she gets to eat an apple from her tree for the first time.
    """
    # L1
    lydia_current_age = 9 # is now 9 years old
    lydia_age_when_planted = 4 # planted a tree when she was 4 years old
    years_since_planted = lydia_current_age - lydia_age_when_planted

    # L2
    years_to_bear_fruit = 7 # takes 7 years for an apple tree to bear fruit
    years_remaining = years_to_bear_fruit - years_since_planted

    # L3
    lydia_age_when_eats = lydia_current_age + years_remaining

    # FA
    answer = lydia_age_when_eats
    return answer