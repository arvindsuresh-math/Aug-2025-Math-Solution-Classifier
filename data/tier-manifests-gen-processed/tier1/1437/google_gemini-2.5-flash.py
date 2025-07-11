def solve():
    """Index: 1437.
    Returns: the total amount Mark paid for the deck and sealant.
    """
    # L1
    deck_width = 30 # 30 feet
    deck_length = 40 # 40 feet
    deck_area = deck_width * deck_length

    # L2
    cost_per_sq_ft = 3 # $3 per square foot
    sealant_cost_per_sq_ft = 1 # $1 per square foot for sealant
    total_cost_per_sq_ft = cost_per_sq_ft + sealant_cost_per_sq_ft

    # L3
    total_paid = deck_area * total_cost_per_sq_ft

    # FA
    answer = total_paid
    return answer