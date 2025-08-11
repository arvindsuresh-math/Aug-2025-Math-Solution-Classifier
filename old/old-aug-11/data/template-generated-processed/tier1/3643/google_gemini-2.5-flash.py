def solve():
    """Index: 3643.
    Returns: the total number of chairs in the bakery.
    """
    # L1
    indoor_tables = 8 # 8 indoor tables
    chairs_per_indoor_table = 3 # Each indoor table has 3 chairs
    indoor_chairs = indoor_tables * chairs_per_indoor_table

    # L2
    outdoor_tables = 12 # 12 outdoor tables
    chairs_per_outdoor_table = 3 # each outdoor table has 3 chairs
    outdoor_chairs = outdoor_tables * chairs_per_outdoor_table

    # L3
    total_chairs = indoor_chairs + outdoor_chairs

    # FA
    answer = total_chairs
    return answer