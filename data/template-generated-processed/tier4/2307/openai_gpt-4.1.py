def solve():
    """Index: 2307.
    Returns: the total cost to fill the sandbox with sand.
    """
    # L1
    sandbox_length = 3 # 3 ft long
    sandbox_width = 3 # 3 ft wide
    sandbox_sq_ft = sandbox_length * sandbox_width

    # L2
    bag_sq_ft = 3 # 3 sq ft bags
    num_bags = sandbox_sq_ft / bag_sq_ft

    # L3
    bag_cost = 4.00 # $4.00 a bag
    total_cost = bag_cost * num_bags

    # FA
    answer = total_cost
    return answer