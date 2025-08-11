def solve():
    """Index: 3757.
    Returns: Jude's current age.
    """
    # L1
    heath_current_age = 16 # Heath is 16 years old today
    years_in_future = 5 # In 5 years
    heath_future_age = heath_current_age + years_in_future

    # L2
    jude_age_multiplier = 3 # 3 times as old as Jude
    jude_future_age = heath_future_age / jude_age_multiplier

    # L3
    age_difference = heath_future_age - jude_future_age

    # L4
    jude_current_age = heath_current_age - age_difference

    # FA
    answer = jude_current_age
    return answer