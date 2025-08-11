def solve():
    """Index: 2496.
    Returns: the number of scarves in the swag bag.
    """
    # L1
    cost_per_earring = 6000 # two diamond earrings that cost $6,000 each
    num_earrings = 2 # two diamond earrings
    total_earring_cost = cost_per_earring * num_earrings

    # L2
    total_swag_bag_value = 20000 # total value of the swag bag is $20,000
    iphone_cost = 2000 # a new iPhone that costs $2,000
    total_scarf_cost = total_swag_bag_value - total_earring_cost - iphone_cost

    # L3
    cost_per_scarf = 1500 # designer scarves that each cost $1,500
    num_scarves = total_scarf_cost / cost_per_scarf

    # FA
    answer = num_scarves
    return answer