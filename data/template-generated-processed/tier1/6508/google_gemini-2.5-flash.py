def solve():
    """Index: 6508.
    Returns: the total number of spoons Lisa now has.
    """
    # L1
    num_children = 4 # 4 children
    spoons_per_child = 3 # 3 spoons when they were babies
    baby_spoons = num_children * spoons_per_child

    # L2
    decorative_spoons = 2 # 2 decorative spoons she created
    old_spoons_total = baby_spoons + decorative_spoons

    # L3
    large_spoons_new_set = 10 # 10 large spoons
    teaspoons_new_set = 15 # 15 teaspoons
    new_spoons_total = large_spoons_new_set + teaspoons_new_set

    # L4
    total_spoons = old_spoons_total + new_spoons_total

    # FA
    answer = total_spoons
    return answer