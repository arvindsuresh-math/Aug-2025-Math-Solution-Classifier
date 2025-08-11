def solve():
    """Index: 2527.
    Returns: the total number of chairs in the cafe.
    """
    # L1
    indoor_tables = 9 # 9 indoor tables
    chairs_per_indoor_table = 10 # 10 chairs
    indoor_chairs = indoor_tables * chairs_per_indoor_table

    # L2
    outdoor_tables = 11 # 11 outdoor tables
    chairs_per_outdoor_table = 3 # 3 chairs
    outdoor_chairs = outdoor_tables * chairs_per_outdoor_table

    # L3
    total_chairs = indoor_chairs + outdoor_chairs

    # FA
    answer = total_chairs
    return answer