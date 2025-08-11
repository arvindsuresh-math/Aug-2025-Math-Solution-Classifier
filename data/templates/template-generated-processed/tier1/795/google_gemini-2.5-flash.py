def solve():
    """Index: 795.
    Returns: the difference in the total number of sandwiches Samson ate on Monday and Tuesday.
    """
    # L1
    sandwiches_lunch_monday = 3 # 3 sandwiches at lunch
    multiplier_dinner = 2 # twice as many at dinner
    sandwiches_dinner_monday = sandwiches_lunch_monday * multiplier_dinner

    # L2
    total_sandwiches_monday = sandwiches_lunch_monday + sandwiches_dinner_monday

    # L3
    sandwiches_breakfast_tuesday = 1 # only ate one sandwich for breakfast
    difference_monday_tuesday = total_sandwiches_monday - sandwiches_breakfast_tuesday

    # FA
    answer = difference_monday_tuesday
    return answer