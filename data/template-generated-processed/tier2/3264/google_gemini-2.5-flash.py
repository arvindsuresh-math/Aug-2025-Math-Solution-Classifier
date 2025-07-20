def solve():
    """Index: 3264.
    Returns: the number of meters of ribbon left from Tom's ribbon.
    """
    # L1
    ribbon_per_gift = 1.5 # Each gift requires 1.5 meters of ribbon
    num_gifts = 8 # Sammy has 8 gifts
    total_ribbon_needed = ribbon_per_gift * num_gifts

    # L2
    toms_ribbon_length = 15 # Tom let her use his 15-meter long ribbon
    ribbon_left = toms_ribbon_length - total_ribbon_needed

    # FA
    answer = ribbon_left
    return answer