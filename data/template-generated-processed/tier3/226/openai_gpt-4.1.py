def solve():
    """Index: 226.
    Returns: the total number of chairs in the hall.
    """
    # L1
    total_tables = 32 # There are 32 tables in a hall
    half_fraction = 1/2 # Half the tables
    tables_with_2_chairs = total_tables * half_fraction

    # L2
    chairs_per_table_2 = 2 # 2 chairs each
    chairs_from_2_chair_tables = tables_with_2_chairs * chairs_per_table_2

    # L3
    tables_with_3_chairs = 5 # 5 have 3 chairs each
    chairs_per_table_3 = 3 # 3 chairs each
    chairs_from_3_chair_tables = tables_with_3_chairs * chairs_per_table_3

    # L4
    tables_with_4_chairs = total_tables - (tables_with_2_chairs + tables_with_3_chairs)

    # L5
    chairs_per_table_4 = 4 # 4 chairs each
    chairs_from_4_chair_tables = tables_with_4_chairs * chairs_per_table_4

    # L6
    total_chairs = chairs_from_2_chair_tables + chairs_from_3_chair_tables + chairs_from_4_chair_tables

    # FA
    answer = total_chairs
    return answer