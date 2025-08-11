def solve():
    """Index: 3427.
    Returns: Annika's current age.
    """
    # L1
    hans_current_age = 8 # Hans is now 8 years old
    years_in_future = 4 # In four years
    hans_age_in_future = hans_current_age + years_in_future

    # L2
    annika_age_multiplier = 3 # three times as old as Hans
    annika_age_in_future = hans_age_in_future * annika_age_multiplier

    # L3
    annika_current_age = annika_age_in_future - years_in_future

    # FA
    answer = annika_current_age
    return answer