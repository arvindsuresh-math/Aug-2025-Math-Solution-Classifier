def solve():
    """Index: 2527.
    Returns: the total number of chairs in the cafe.
    """
    # L1
    num_indoor_tables = 9 # 9 indoor tables
    chairs_per_indoor_table = 10 # each indoor table has 10 chairs
    indoor_chairs = num_indoor_tables * chairs_per_indoor_table

    # L2
    num_outdoor_tables = 11 # 11 outdoor tables
    chairs_per_outdoor_table = 3 # each outdoor table has 3 chairs
    outdoor_chairs = num_outdoor_tables * chairs_per_outdoor_table

    # L3
    total_chairs = indoor_chairs + outdoor_chairs

    # FA
    answer = total_chairs
    return answer