def solve():
    """Index: 2307.
    Returns: the total cost to fill up the sandbox.
    """
    # L1
    sandbox_length = 3 # 3 ft long
    sandbox_width = 3 # 3 ft wide
    sandbox_sq_footage = sandbox_length * sandbox_width

    # L2
    sq_ft_per_bag = 3 # 3 sq ft bags
    num_bags = sandbox_sq_footage / sq_ft_per_bag

    # L3
    cost_per_bag = 4.00 # $4.00 a bag
    total_cost = cost_per_bag * num_bags

    # FA
    answer = total_cost
    return answer