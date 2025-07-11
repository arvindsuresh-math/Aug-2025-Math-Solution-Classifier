def solve():
    """Index: 2891.
    Returns: the height of the hill.
    """
    # L2
    base_height_above_seabed = 300 # The base of a hill located beside a river is 300m above the seabed.
    multiplier = 4 # If this depth is a quarter of the vertical distance
    distance_riverbed_to_peak = base_height_above_seabed * multiplier

    # L3
    hill_height = distance_riverbed_to_peak - base_height_above_seabed

    # FA
    answer = hill_height
    return answer