def solve():
    """Index: 4136.
    Returns: the remaining capacity of the grocery bag.
    """
    # L1
    green_beans_weight = 4 # 4 pounds of green beans
    carrot_multiplier = 2 # twice the amount of carrots
    carrots_weight = green_beans_weight * carrot_multiplier

    # L2
    milk_weight = 6 # 6 pounds milk
    total_groceries_weight = milk_weight + carrots_weight + green_beans_weight

    # L3
    bag_weight_limit = 20 # maximum of twenty pounds
    remaining_capacity = bag_weight_limit - total_groceries_weight

    # FA
    answer = remaining_capacity
    return answer