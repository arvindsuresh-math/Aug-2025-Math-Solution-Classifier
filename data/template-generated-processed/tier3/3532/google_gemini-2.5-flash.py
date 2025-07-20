def solve():
    """Index: 3532.
    Returns: the number of people Donna can feed.
    """
    # L1
    initial_sandwiches = 20 # makes 20 sandwiches
    first_cut_multiplier = 2 # cuts them in half
    portions_after_first_halving = initial_sandwiches * first_cut_multiplier

    # L2
    second_cut_multiplier = 2 # cutting them in half again
    total_portions = portions_after_first_halving * second_cut_multiplier

    # L3
    portions_per_person = 8 # gives everyone 8 portions
    num_people_fed = total_portions / portions_per_person

    # FA
    answer = num_people_fed
    return answer