def solve():
    """Index: 6358.
    Returns: the total cost for one sandwich and one juice.
    """
    # L1
    total_juice_cost = 10 # $10 in total
    num_juices = 5 # five juices
    cost_per_juice = total_juice_cost / num_juices

    # L2
    total_sandwich_cost = 6 # $6 in total
    num_sandwiches = 2 # two sandwiches
    cost_per_sandwich = total_sandwich_cost / num_sandwiches

    # L3
    total_cost_one_of_each = cost_per_juice + cost_per_sandwich

    # FA
    answer = total_cost_one_of_each
    return answer