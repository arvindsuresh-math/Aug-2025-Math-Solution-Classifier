def solve():
    """Index: 4835.
    Returns: the total amount Sofia will pay for all items.
    """
    # L1
    shirt_cost = 7 # A shirt costs $7
    num_shirts = 2 # 2 shirts
    cost_two_shirts = shirt_cost * num_shirts

    # L2
    shoes_extra_cost = 3 # shoes is $3 more than the shirt
    cost_shoes = shirt_cost + shoes_extra_cost

    # L3
    cost_shirts_and_shoes = cost_two_shirts + cost_shoes

    # L4
    bag_divisor = 2 # half the total price
    cost_bag = cost_shirts_and_shoes / bag_divisor

    # L5
    total_cost = cost_two_shirts + cost_shoes + cost_bag

    # FA
    answer = total_cost
    return answer