def solve():
    """Index: 1078.
    Returns: the total number of fish at the wedding reception.
    """
    # L1
    num_tables = 32 # 32 tables
    fish_per_bowl_standard = 2 # 2 fish
    fish_standard_tables = num_tables * fish_per_bowl_standard

    # L2
    extra_fish_on_one_table = 1 # one table that has 3 fish (which is 1 more than the standard 2)
    total_fish = fish_standard_tables + extra_fish_on_one_table

    # FA
    answer = total_fish
    return answer