def solve():
    """Index: 1437.
    Returns: the total amount Mark paid for the deck and sealant.
    """
    # L1
    length = 30 # 30 feet
    width = 40 # 40 feet
    area = length * width

    # L2
    cost_per_sqft = 3 # $3 per square foot
    sealant_per_sqft = 1 # extra $1 per square foot for sealant
    total_per_sqft = cost_per_sqft + sealant_per_sqft

    # L3
    total_cost = area * total_per_sqft

    # FA
    answer = total_cost
    return answer