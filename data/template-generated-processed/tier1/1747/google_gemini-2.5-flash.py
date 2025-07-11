def solve():
    """Index: 1747.
    Returns: the number of more marbles Markus has than Mara.
    """
    # L1
    marbles_per_bag_mara = 2 # 2 marbles in each bag
    num_bags_mara = 12 # 12 bags
    total_marbles_mara = marbles_per_bag_mara * num_bags_mara

    # L2
    num_bags_markus = 2 # 2 bags
    marbles_per_bag_markus = 13 # 13 marbles in each bag
    total_marbles_markus = num_bags_markus * marbles_per_bag_markus

    # L3
    difference_marbles = total_marbles_markus - total_marbles_mara

    # FA
    answer = difference_marbles
    return answer