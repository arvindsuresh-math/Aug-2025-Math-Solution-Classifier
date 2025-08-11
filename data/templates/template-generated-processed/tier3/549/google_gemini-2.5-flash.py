def solve():
    """Index: 549.
    Returns: the total number of legs of furniture Kenzo has remaining.
    """
    # L1
    disposed_percentage_numerator = 40 # 40% of the chairs are damaged
    disposed_percentage_denominator = 100 # 40% of the chairs are damaged
    initial_chairs = 80 # 80 office chairs
    disposed_chairs = disposed_percentage_numerator / disposed_percentage_denominator * initial_chairs

    # L2
    remaining_chairs = initial_chairs - disposed_chairs

    # L3
    legs_per_chair = 5 # five legs each
    chair_legs = remaining_chairs * legs_per_chair

    # L4
    num_tables = 20 # 20 round tables
    legs_per_table = 3 # three legs each
    table_legs = num_tables * legs_per_table

    # L5
    total_legs = table_legs + chair_legs

    # FA
    answer = total_legs
    return answer