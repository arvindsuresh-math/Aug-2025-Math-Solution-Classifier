def solve():
    """Index: 3070.
    Returns: the number of marbles Brianna had remaining.
    """
    # L1
    times_given_away = 2 # twice as many marbles
    lost_marbles = 4 # lost four marbles
    marbles_given_away = times_given_away * lost_marbles

    # L2
    half_divisor = 2 # half as many marbles
    marbles_dog_ate = lost_marbles / half_divisor

    # L3
    initial_marbles = 24 # a bag of 24 marbles
    marbles_remaining = initial_marbles - lost_marbles - marbles_given_away - marbles_dog_ate

    # FA
    answer = marbles_remaining
    return answer