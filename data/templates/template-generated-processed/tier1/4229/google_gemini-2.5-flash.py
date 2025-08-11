def solve():
    """Index: 4229.
    Returns: the number of matches Nate has left.
    """
    # L1
    matches_dropped_creek = 10 # He drops 10 in a creek
    dog_eats_multiplier = 2 # his dog eats twice as many
    matches_dog_eats = matches_dropped_creek * dog_eats_multiplier

    # L2
    initial_matches = 70 # Nate starts his camping trip with 70 matches
    remaining_matches = initial_matches - matches_dropped_creek - matches_dog_eats

    # FA
    answer = remaining_matches
    return answer