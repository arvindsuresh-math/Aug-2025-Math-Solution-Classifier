def solve():
    """Index: 6438.
    Returns: the number of tables the woodworker has made.
    """
    # L1
    num_chairs = 6 # built 6 chairs
    legs_per_chair = 4 # WK
    legs_for_chairs = num_chairs * legs_per_chair

    # L2
    total_legs_made = 40 # total of 40 furniture legs
    legs_for_tables = total_legs_made - legs_for_chairs

    # L3
    legs_per_table = 4 # WK
    num_tables = legs_for_tables / legs_per_table

    # FA
    answer = num_tables
    return answer