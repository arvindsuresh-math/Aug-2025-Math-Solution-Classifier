def solve():
    """Index: 6765.
    Returns: the total number of frogs Hunter saw in the pond.
    """
    # L1
    frogs_on_lily_pads = 5 # 5 frogs sitting on top lily pads
    frogs_on_logs = 3 # Three more frogs climbed out of the water onto logs
    adult_frogs = frogs_on_lily_pads + frogs_on_logs

    # L2
    num_dozen_baby_frogs = 2 # two dozen baby frogs
    dozen = 12 # WK
    baby_frogs = num_dozen_baby_frogs * dozen

    # L3
    total_frogs = adult_frogs + baby_frogs

    # FA
    answer = total_frogs
    return answer