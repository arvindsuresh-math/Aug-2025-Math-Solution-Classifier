def solve():
    """Index: 1767.
    Returns: the number of chives Juvy will plant.
    """
    # L1
    parsley_rows = 3 # parsley in the first 3 rows
    rosemary_rows = 2 # rosemary in the last two rows
    non_chive_rows = parsley_rows + rosemary_rows

    # L2
    total_rows = 20 # garden has 20 rows
    chive_rows = total_rows - non_chive_rows

    # L3
    plants_per_row = 10 # 10 plants in each row
    chives_planted = chive_rows * plants_per_row

    # FA
    answer = chives_planted
    return answer