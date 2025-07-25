def solve():
    """Index: 4930.
    Returns: the total number of trees cut down.
    """
    # L1
    days_alone = 2 # In the first 2 days
    trees_per_day_alone = 20 # 20 trees each day
    trees_cut_alone = days_alone * trees_per_day_alone

    # L2
    original_trees_per_day = 20 # 20 trees each day
    reduction_percent = 0.2 # 20% fewer trees
    trees_fewer_per_brother = original_trees_per_day * reduction_percent

    # L3
    trees_per_day_per_brother = original_trees_per_day - trees_fewer_per_brother

    # L4
    num_brothers = 2 # his 2 brothers
    trees_per_day_with_brothers = original_trees_per_day + trees_per_day_per_brother * num_brothers

    # L5
    days_with_brothers = 3 # For the next 3 days
    total_trees_cut = trees_cut_alone + trees_per_day_with_brothers * days_with_brothers

    # FA
    answer = total_trees_cut
    return answer