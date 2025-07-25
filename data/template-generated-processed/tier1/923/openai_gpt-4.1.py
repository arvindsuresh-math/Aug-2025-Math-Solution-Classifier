def solve():
    """Index: 923.
    Returns: the total cost of John's quilt.
    """
    # L1
    length_feet = 7 # 7 foot
    width_feet = 8 # 8-foot
    area_sqft = length_feet * width_feet

    # L2
    cost_per_sqft = 40 # $40 per square foot
    total_cost = cost_per_sqft * area_sqft

    # FA
    answer = total_cost
    return answer