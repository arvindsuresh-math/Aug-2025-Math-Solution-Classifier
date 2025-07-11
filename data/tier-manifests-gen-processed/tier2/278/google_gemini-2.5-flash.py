def solve():
    """Index: 278.
    Returns: the total cost of the property.
    """
    # L1
    house_area = 2400 # 2,400 sq ft
    barn_area = 1000 # 1,000 sq ft
    total_area = house_area + barn_area

    # L2
    price_per_sq_ft = 98 # $98 per square foot
    total_property_cost = price_per_sq_ft * total_area

    # FA
    answer = total_property_cost
    return answer