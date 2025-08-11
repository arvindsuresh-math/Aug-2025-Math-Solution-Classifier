def solve():
    """Index: 2203.
    Returns: the number of eggs Ben has now.
    """
    # L1
    eggs_morning = 4 # ate 4 eggs in the morning
    eggs_afternoon = 3 # and 3 in the afternoon
    total_eaten_yesterday = eggs_morning + eggs_afternoon

    # L2
    initial_eggs = 20 # 20 eggs in the fridge
    eggs_remaining = initial_eggs - total_eaten_yesterday

    # FA
    answer = eggs_remaining
    return answer