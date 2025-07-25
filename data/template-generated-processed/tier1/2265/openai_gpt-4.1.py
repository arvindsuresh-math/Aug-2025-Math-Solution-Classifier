def solve():
    """Index: 2265.
    Returns: the total number of people who dropped before finishing the race.
    """
    # L1
    initial_racers = 50 # 50 racers in a bicycle charity race at the beginning
    joined_racers = 30 # 30 more racers joined the race
    racers_after_join = initial_racers + joined_racers

    # L2
    doubling_factor = 2 # doubled after another 30 minutes
    total_racers = racers_after_join * doubling_factor

    # L3
    finished_racers = 130 # only 130 people finished the race
    dropped_racers = total_racers - finished_racers

    # FA
    answer = dropped_racers
    return answer