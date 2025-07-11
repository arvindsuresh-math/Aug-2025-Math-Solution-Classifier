def solve():
    """Index: 1712.
    Returns: the total amount Marlene will pay for the shirts.
    """
    # L1
    dozen = 12 # WK
    half_divisor = 2 # half a dozen of shirts
    num_shirts = dozen / half_divisor

    # L2
    regular_price = 50 # The regular price of a shirt is $50
    discount_percentage_numerator = 20 # 20% discount
    percentage_denominator = 100 # WK
    discount_amount = regular_price * discount_percentage_numerator / percentage_denominator

    # L3
    price_per_shirt = regular_price - discount_amount

    # L4
    total_cost = price_per_shirt * num_shirts

    # FA
    answer = total_cost
    return answer