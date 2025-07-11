def solve():
    """Index: 494.
    Returns: the amount the smaller house is being expanded by in sq. ft.
    """
    # L1
    larger_house_sqft = 7300 # a 7,300 sq. ft. house
    smaller_house_sqft = 5200 # a 5,200 sq. ft. house
    original_total_sqft = larger_house_sqft + smaller_house_sqft

    # L2
    new_total_sqft = 16000 # new total square footage of both houses is 16,000 sq. ft.
    expansion_amount = new_total_sqft - original_total_sqft

    # FA
    answer = expansion_amount
    return answer