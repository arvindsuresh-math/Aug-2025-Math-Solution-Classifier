def solve():
    """Index: 2135.
    Returns: the average weight of Janele's cats.
    """
    # L1
    cat1_weight = 12.0 # The first two weigh 12 pounds each
    cat2_weight = 12.0 # The first two weigh 12 pounds each
    cat3_weight = 14.7 # The third weighs 14.7 pounds
    cat4_weight = 9.3 # the fourth weighs 9.3 pounds
    total_weight = cat1_weight + cat2_weight + cat3_weight + cat4_weight

    # L2
    num_cats = 4 # She has 4 of them
    average_weight = total_weight / num_cats

    # FA
    answer = average_weight
    return answer