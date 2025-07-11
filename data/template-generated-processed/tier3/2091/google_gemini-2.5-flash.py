def solve():
    """Index: 2091.
    Returns: the amount Shara saved.
    """
    # L1
    original_percentage = 100 # WK
    discount_percentage = 8 # an 8% discount
    paid_percentage = original_percentage - discount_percentage

    # L2
    paid_amount = 184 # paid $184
    value_per_percent = paid_amount / paid_percentage

    # L3
    amount_saved = value_per_percent * discount_percentage

    # FA
    answer = amount_saved
    return answer