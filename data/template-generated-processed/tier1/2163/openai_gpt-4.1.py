def solve():
    """Index: 2163.
    Returns: the total number of musical instruments Miles owns.
    """
    # L1
    num_fingers = 10 # Miles has fingers (human)
    trumpets_fewer = 3 # three fewer trumpets than he has fingers
    trumpets = num_fingers - trumpets_fewer

    # L2
    num_hands = 2 # Miles has hands (human)
    guitars_more = 2 # two more guitars than he has hands
    guitars = num_hands + guitars_more

    # L3
    num_heads = 1 # Miles has heads (human)
    trombones_more = 2 # two more trombones than he has heads
    trombones = trombones_more + num_heads

    # L4
    french_horns_fewer = 1 # one fewer French horn than he has guitars
    french_horns = guitars - french_horns_fewer

    # L5
    total_instruments = trumpets + guitars + trombones + french_horns

    # FA
    answer = total_instruments
    return answer