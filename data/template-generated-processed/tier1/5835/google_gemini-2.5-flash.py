def solve():
    """Index: 5835.
    Returns: the cost of a single necklace.
    """
    # L3
    total_cost = 240000 # a total of $240,000
    num_necklaces_bought = 3 # three necklaces
    earrings_multiplier = 3 # three times as expensive as any one necklace
    # The sum of coefficients for 'x' on the left side of the equation (1x for each of the 3 necklaces + 3x for earrings)
    lhs_coefficient_sum = num_necklaces_bought + earrings_multiplier

    # L5
    # Solving the equation: lhs_coefficient_sum * x = total_cost
    price_single_necklace = total_cost / lhs_coefficient_sum

    # FA
    answer = price_single_necklace
    return answer