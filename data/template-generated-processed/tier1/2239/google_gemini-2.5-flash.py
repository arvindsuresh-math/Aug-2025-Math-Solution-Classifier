def solve():
    """Index: 2239.
    Returns: the total number of oranges for Philip to pick.
    """
    # L1
    betty_oranges = 15 # Betty picked 15 oranges
    bill_oranges = 12 # Bill picked 12 oranges
    combined_betty_bill = betty_oranges + bill_oranges

    # L2
    frank_multiplier = 3 # three times the number
    frank_oranges = frank_multiplier * combined_betty_bill

    # L3
    seeds_per_orange = 2 # 2 seeds from each of his oranges
    total_trees = seeds_per_orange * frank_oranges

    # L4
    oranges_per_tree = 5 # 5 oranges for Frank's son Philip to pick
    philip_total_oranges = total_trees * oranges_per_tree

    # FA
    answer = philip_total_oranges
    return answer