def solve():
    """Index: 4926.
    Returns: the number of carrots planted per hour.
    """
    # L1
    rows = 400 # 400 rows of carrots
    plants_per_row = 300 # 300 plants in each row
    total_plants = rows * plants_per_row

    # L2
    hours_spent = 20 # it took him 20 hours
    plants_per_hour = total_plants / hours_spent

    # FA
    answer = plants_per_hour
    return answer