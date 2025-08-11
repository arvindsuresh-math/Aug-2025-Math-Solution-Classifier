def solve():
    """Index: 6122.
    Returns: the number of apples Ella has left.
    """
    # L1
    num_bags_group1 = 4 # 4 bags
    apples_per_bag_group1 = 20 # 20 apples in each bag
    apples_group1 = num_bags_group1 * apples_per_bag_group1

    # L2
    num_bags_group2 = 6 # six bags
    apples_per_bag_group2 = 25 # 25 apples in each bag
    apples_group2 = num_bags_group2 * apples_per_bag_group2

    # L3
    total_apples_initial = apples_group1 + apples_group2

    # L4
    apples_sold = 200 # sells 200 apples
    apples_left = total_apples_initial - apples_sold

    # FA
    answer = apples_left
    return answer