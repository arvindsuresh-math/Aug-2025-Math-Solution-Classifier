from fractions import Fraction

def solve():
    """Index: 226.
    Returns: the total number of chairs in the hall.
    """
    # L1
    total_tables = 32 # 32 tables in a hall
    half_fraction = Fraction(1, 2) # Half the tables
    tables_half = total_tables * half_fraction

    # L2
    chairs_per_half_table = 2 # have 2 chairs each
    chairs_from_half_tables = tables_half * chairs_per_half_table

    # L3
    tables_with_3_chairs = 5 # 5 have 3 chairs each
    chairs_per_3_chair_table = 3 # 3 chairs each
    chairs_from_3_chair_tables = tables_with_3_chairs * chairs_per_3_chair_table

    # L4
    remaining_tables = total_tables - (tables_half + tables_with_3_chairs)

    # L5
    chairs_per_4_chair_table = 4 # the rest have 4 chairs each
    chairs_from_remaining_tables = remaining_tables * chairs_per_4_chair_table

    # L6
    total_chairs = chairs_from_half_tables + chairs_from_3_chair_tables + chairs_from_remaining_tables

    # FA
    answer = total_chairs
    return answer