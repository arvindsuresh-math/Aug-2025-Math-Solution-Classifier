def solve():
    """Index: 6485.
    Returns: the current age of the father.
    """
    # L1
    son_age_next_year = 8 # son will be eight years old
    years_from_now = 1 # WK
    son_current_age = son_age_next_year - years_from_now

    # L2
    age_multiplier = 5 # five times that of my son
    father_current_age = age_multiplier * son_current_age

    # FA
    answer = father_current_age
    return answer