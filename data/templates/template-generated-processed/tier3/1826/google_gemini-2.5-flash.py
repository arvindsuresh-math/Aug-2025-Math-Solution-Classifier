def solve():
    """Index: 1826.
    Returns: the number of pushups Miriam does on Friday.
    """
    # L1
    monday_pushups = 5 # On Monday she does 5 push-ups
    tuesday_pushups = 7 # On Tuesday she does 7 push-ups
    monday_tuesday_total = monday_pushups + tuesday_pushups

    # L2
    wednesday_multiplier = 2 # twice as many push-ups
    wednesday_pushups = tuesday_pushups * wednesday_multiplier

    # L3
    total_first_three_days = wednesday_pushups + monday_tuesday_total

    # L4
    thursday_fraction = 0.5 # half the number of total pushups
    thursday_pushups = thursday_fraction * total_first_three_days

    # L5
    friday_pushups = monday_pushups + tuesday_pushups + wednesday_pushups + thursday_pushups

    # FA
    answer = friday_pushups
    return answer