def solve():
    """Index: 2265.
    Returns: the total number of people who dropped before finishing the race.
    """
    # L1
    initial_racers = 50 # 50 racers in a bicycle charity race
    racers_joined = 30 # 30 more racers joined the race
    racers_after_joining = initial_racers + racers_joined

    # L2
    doubling_factor = 2 # The total number of racers doubled
    racers_after_doubling = racers_after_joining * doubling_factor

    # L3
    racers_finished = 130 # only 130 people finished the race
    dropped_racers = racers_after_doubling - racers_finished

    # FA
    answer = dropped_racers
    return answer