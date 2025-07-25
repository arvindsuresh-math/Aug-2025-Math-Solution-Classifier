def solve():
    """Index: 2203.
    Returns: the number of eggs Ben has now.
    """
    # L1
    eggs_eaten_morning = 4 # ate 4 eggs in the morning
    eggs_eaten_afternoon = 3 # ate 3 in the afternoon
    eggs_eaten_yesterday = eggs_eaten_morning + eggs_eaten_afternoon

    # L2
    eggs_initial = 20 # Ben has 20 eggs in the fridge
    eggs_left = eggs_initial - eggs_eaten_yesterday

    # FA
    answer = eggs_left
    return answer