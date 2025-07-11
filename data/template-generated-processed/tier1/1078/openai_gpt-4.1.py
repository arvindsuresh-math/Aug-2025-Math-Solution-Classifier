def solve():
    """Index: 1078.
    Returns: the total number of fish at Glenda's wedding reception.
    """
    # L1
    num_tables = 32 # There are 32 tables
    fish_per_table = 2 # 2 fish in a bowl on each
    fish_regular_tables = num_tables * fish_per_table

    # L2
    extra_fish = 1 # one table has an additional fish
    total_fish = fish_regular_tables + extra_fish

    # FA
    answer = total_fish
    return answer