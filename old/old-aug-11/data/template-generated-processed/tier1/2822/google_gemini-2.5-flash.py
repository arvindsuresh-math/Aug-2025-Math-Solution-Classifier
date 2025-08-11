def solve():
    """Index: 2822.
    Returns: Jennifer's sister's current age.
    """
    # L1
    jennifer_age_in_future = 30 # Jennifer will be 30 years old
    jordana_age_multiplier = 3 # three times as old Jennifer
    jordana_age_in_future = jordana_age_multiplier * jennifer_age_in_future

    # L2
    years_from_now = 10 # in ten years
    jordana_current_age = jordana_age_in_future - years_from_now

    # FA
    answer = jordana_current_age
    return answer