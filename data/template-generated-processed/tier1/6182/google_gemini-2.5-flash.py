def solve():
    """Index: 6182.
    Returns: the total number of chairs in the office canteen.
    """
    # L1
    num_round_tables = 2 # 2 round tables
    chairs_per_round_table = 6 # 6 chairs
    chairs_round_tables = num_round_tables * chairs_per_round_table

    # L2
    num_rectangular_tables = 2 # 2 rectangular tables
    chairs_per_rectangular_table = 7 # 7 chairs
    chairs_rectangular_tables = num_rectangular_tables * chairs_per_rectangular_table

    # L3
    total_chairs = chairs_round_tables + chairs_rectangular_tables

    # FA
    answer = total_chairs
    return answer