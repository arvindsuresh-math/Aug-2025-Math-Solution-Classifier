def solve():
    """Index: 4834.
    Returns: the total feet of wood needed for the rungs.
    """
    # L1
    inches_per_foot = 12 # WK
    rung_spacing_inches = 6 # they are 6 inches apart
    rungs_per_foot = inches_per_foot / rung_spacing_inches

    # L2
    climb_height_feet = 50 # climb 50 feet
    total_rungs_needed = climb_height_feet * rungs_per_foot

    # L3
    rung_length_inches = 18 # Each rung of the ladder is 18 inches long
    rung_length_feet = rung_length_inches / inches_per_foot

    # L4
    total_wood_feet = rung_length_feet * total_rungs_needed

    # FA
    answer = total_wood_feet
    return answer