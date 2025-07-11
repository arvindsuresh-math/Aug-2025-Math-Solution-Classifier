def solve():
    """Index: 2239.
    Returns: the total number of oranges Philip can pick from the trees.
    """
    # L1
    betty_oranges = 15 # Betty picked 15 oranges
    bill_oranges = 12 # Bill picked 12 oranges
    betty_bill_total = betty_oranges + bill_oranges

    # L2
    frank_multiplier = 3 # Frank picked three times the number
    frank_oranges = frank_multiplier * betty_bill_total

    # L3
    seeds_per_orange = 2 # planted 2 seeds from each of his oranges
    total_seeds = seeds_per_orange * frank_oranges
    # Each seed becomes a tree, so total_seeds = number of trees

    # L4
    oranges_per_tree = 5 # each orange tree contains 5 oranges
    philip_total_oranges = total_seeds * oranges_per_tree

    # FA
    answer = philip_total_oranges
    return answer