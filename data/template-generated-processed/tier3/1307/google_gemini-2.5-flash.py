def solve():
    """Index: 1307.
    Returns: Sarah's age.
    """
    # L1
    ana_future_age = 15 # Ana will be 15 in 3 years
    years_to_subtract = 3 # in 3 years
    ana_current_age = ana_future_age - years_to_subtract

    # L2
    divisor_for_billy = 2 # Billy is half Ana's age
    billy_age = ana_current_age / divisor_for_billy

    # L3
    mark_age_difference = 4 # Mark is four years older than Billy
    mark_age = billy_age + mark_age_difference

    # L4
    sarah_multiplier = 3 # three times Mark's age
    triple_mark_age = mark_age * sarah_multiplier

    # L5
    sarah_subtraction = 4 # minus 4
    sarah_age = triple_mark_age - sarah_subtraction

    # FA
    answer = sarah_age
    return answer