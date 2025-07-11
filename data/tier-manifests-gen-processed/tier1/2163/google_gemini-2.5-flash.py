def solve():
    """Index: 2163.
    Returns: the total number of musical instruments Miles owns.
    """
    # L1
    fingers = 10 # WK
    fewer_trumpets = 3 # three fewer trumpets
    num_trumpets = fingers - fewer_trumpets

    # L2
    hands = 2 # WK
    more_guitars = 2 # two more guitars
    num_guitars = hands + more_guitars

    # L3
    heads = 1 # WK
    more_trombones = 2 # two more trombones
    num_trombones = more_trombones + heads

    # L4
    fewer_french_horn = 1 # one fewer French horn
    num_french_horns = num_guitars - fewer_french_horn

    # L5
    total_instruments = num_trumpets + num_guitars + num_trombones + num_french_horns

    # FA
    answer = total_instruments
    return answer