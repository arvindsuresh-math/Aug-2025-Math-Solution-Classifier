def solve():
    """Index: 2574.
    Returns: the number of laps Joel can swim.
    """
    # L1
    yvonne_laps = 10 # Yvonne swims 10 laps
    sister_divisor = 2 # half as many laps
    sister_laps = yvonne_laps / sister_divisor

    # L2
    joel_multiplier = 3 # three times the number of laps
    joel_laps = joel_multiplier * sister_laps

    # FA
    answer = joel_laps
    return answer