def solve():
    """Index: 1377.
    Returns: the average number of ducks the three bought.
    """
    # L1
    adelaide_ducks = 30 # Adelaide bought 30 ducks
    adelaide_ephraim_ratio = 2 # twice the number of ducks that Ephraim bought
    ephraim_ducks = adelaide_ducks / adelaide_ephraim_ratio

    # L2
    ephraim_kolton_difference = 45 # Ephraim bought 45 fewer ducks than Kolton
    kolton_ducks = ephraim_kolton_difference + ephraim_ducks

    # L3
    total_ducks = kolton_ducks + ephraim_ducks + adelaide_ducks

    # L4
    number_of_people = 3 # the three bought
    average_ducks = total_ducks / number_of_people

    # FA
    answer = average_ducks
    return answer