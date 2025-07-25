def solve():
    """Index: 3071.
    Returns: the number of hours Claire spent crafting.
    """
    # L1
    total_hours_in_day = 24 # WK
    cleaning_hours = 4 # four hours to clean
    cooking_hours = 2 # two hours to cook
    sleeping_hours = 8 # sleeps eight hours
    crafting_and_tailoring_hours = total_hours_in_day - cleaning_hours - cooking_hours - sleeping_hours

    # L2
    split_factor = 0.5 # WK
    crafting_hours = crafting_and_tailoring_hours * split_factor

    # FA
    answer = crafting_hours
    return answer