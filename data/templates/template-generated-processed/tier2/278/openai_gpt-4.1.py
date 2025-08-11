def solve():
    """Index: 278.
    Returns: the total price of the property.
    """
    # L1
    house_sqft = 2400 # The house is 2,400 sq ft
    barn_sqft = 1000 # the barn out back is 1,000 sq ft
    total_sqft = house_sqft + barn_sqft

    # L2
    price_per_sqft = 98 # price of a home is $98 per square foot
    property_cost = price_per_sqft * total_sqft

    # FA
    answer = property_cost
    return answer