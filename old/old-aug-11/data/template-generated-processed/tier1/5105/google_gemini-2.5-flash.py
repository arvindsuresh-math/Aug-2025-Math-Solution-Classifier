def solve():
    """Index: 5105.
    Returns: the total number of logs Jerry gets.
    """
    # L1
    logs_per_pine_tree = 80 # Each pine tree makes 80 logs
    num_pine_trees = 8 # 8 pine trees
    total_pine_logs = logs_per_pine_tree * num_pine_trees

    # L2
    logs_per_maple_tree = 60 # each maple tree makes 60 logs
    num_maple_trees = 3 # 3 maple trees
    total_maple_logs = logs_per_maple_tree * num_maple_trees

    # L3
    logs_per_walnut_tree = 100 # each walnut tree makes 100 logs
    num_walnut_trees = 4 # 4 walnut trees
    total_walnut_logs = logs_per_walnut_tree * num_walnut_trees

    # L4
    total_logs = total_pine_logs + total_maple_logs + total_walnut_logs

    # FA
    answer = total_logs
    return answer