def solve():
    """Index: 6352.
    Returns: the total number of hours Mary can keep warm.
    """
    # L1
    sticks_per_chair = 6 # Chairs make 6 sticks of wood
    num_chairs = 18 # chops up 18 chairs
    total_sticks_from_chairs = sticks_per_chair * num_chairs

    # L2
    sticks_per_table = 9 # tables make 9 sticks of wood
    num_tables = 6 # 6 tables
    total_sticks_from_tables = sticks_per_table * num_tables

    # L3
    sticks_per_stool = 2 # stools make 2 sticks of wood
    num_stools = 4 # 4 stools
    total_sticks_from_stools = sticks_per_stool * num_stools

    # L4
    total_sticks = total_sticks_from_chairs + total_sticks_from_tables + total_sticks_from_stools

    # L5
    sticks_per_hour = 5 # burn 5 sticks of wood per hour
    total_hours = total_sticks / sticks_per_hour

    # FA
    answer = total_hours
    return answer