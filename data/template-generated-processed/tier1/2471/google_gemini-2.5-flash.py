def solve():
    """Index: 2471.
    Returns: the amount John pays after the discount.
    """
    # L1
    cost_per_night = 250 # $250 a night
    num_nights = 3 # 3 nights
    total_cost_before_discount = cost_per_night * num_nights

    # L2
    discount_amount = 100 # $100 discount
    final_payment = total_cost_before_discount - discount_amount

    # FA
    answer = final_payment
    return answer