def solve():
    """Index: 5226.
    Returns: the total capacity of all the tables at the party venue.
    """
    # L1
    num_tables_type1 = 4 # 4 tables
    capacity_per_table_type1 = 6 # seat 6 people each
    capacity_type1 = num_tables_type1 * capacity_per_table_type1

    # L2
    num_tables_type2 = 16 # 16 tables
    capacity_per_table_type2 = 4 # seat 4 people each
    capacity_type2 = num_tables_type2 * capacity_per_table_type2

    # L3
    num_tables_type3 = 8 # 8 round tables
    capacity_per_table_type3 = 10 # seat 10 people each
    capacity_type3 = num_tables_type3 * capacity_per_table_type3

    # L4
    total_capacity = capacity_type1 + capacity_type2 + capacity_type3

    # FA
    answer = total_capacity
    return answer