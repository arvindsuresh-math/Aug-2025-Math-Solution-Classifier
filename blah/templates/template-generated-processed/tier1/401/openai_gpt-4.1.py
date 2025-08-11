def solve():
    """Index: 401.
    Returns: the number of pounds of firewood collected by Ela.
    """
    # L1
    kimberley_pounds = 10 # Kimberley collects ten pounds of firewood
    houston_pounds = 12 # Houston collects 12 pounds of firewood
    kimberley_houston_total = kimberley_pounds + houston_pounds

    # L2
    total_collected = 35 # the three of them managed to collect a total of 35 pounds
    ela_pounds = total_collected - kimberley_houston_total

    # FA
    answer = ela_pounds
    return answer