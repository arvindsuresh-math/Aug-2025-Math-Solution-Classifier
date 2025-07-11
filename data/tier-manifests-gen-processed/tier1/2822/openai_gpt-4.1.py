def solve():
    """Index: 2822.
    Returns: Jennifer's sister Jordana's current age.
    """
    # L1
    jennifer_future_age = 30 # Jennifer will be 30 years old in ten years
    jordana_multiplier = 3 # Jordana will be three times as old as Jennifer
    jordana_future_age = jordana_multiplier * jennifer_future_age

    # L2
    years_until_future = 10 # in ten years
    jordana_current_age = jordana_future_age - years_until_future

    # FA
    answer = jordana_current_age
    return answer