def solve():
    """Index: 795.
    Returns: how many more sandwiches Samson ate on Monday than Tuesday.
    """
    # L1
    sandwiches_lunch_monday = 3 # ate 3 sandwiches at lunch
    dinner_multiplier = 2 # ate twice as many at dinner
    sandwiches_dinner_monday = sandwiches_lunch_monday * dinner_multiplier

    # L2
    sandwiches_monday_total = sandwiches_lunch_monday + sandwiches_dinner_monday

    # L3
    sandwiches_tuesday_breakfast = 1 # only ate one sandwich for breakfast
    difference = sandwiches_monday_total - sandwiches_tuesday_breakfast

    # FA
    answer = difference
    return answer