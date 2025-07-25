def solve():
    """Index: 6251.
    Returns: the number of peaches put in the knapsack.
    """
    # L1
    num_dozen_peaches = 5 # five dozen peaches
    dozen = 12 # WK
    total_peaches_initial = num_dozen_peaches * dozen

    # L3
    cloth_bag_peaches_unit = 2 # half as many peaches as she placed in each of the two cloth bags (implies cloth bag has 2x knapsack)
    num_cloth_bags = 2 # two identically-sized cloth bags
    total_units = 1 + (num_cloth_bags * cloth_bag_peaches_unit)

    # L5
    peaches_in_knapsack = total_peaches_initial / total_units

    # FA
    answer = peaches_in_knapsack
    return answer