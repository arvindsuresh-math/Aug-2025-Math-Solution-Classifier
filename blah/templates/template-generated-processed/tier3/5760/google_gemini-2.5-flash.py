def solve():
    """Index: 5760.
    Returns: the total amount to pay for ice cream and juice.
    """
    # L1
    original_ice_cream_price = 12 # original price of $12
    discount_amount = 2 # $2 less
    current_ice_cream_price = original_ice_cream_price - discount_amount

    # L2
    number_of_tubs = 2 # buy two tubs of ice cream
    total_ice_cream_cost = current_ice_cream_price * number_of_tubs

    # L3
    total_cans_to_buy = 10 # 10 cans of juice
    cans_per_set = 5 # $2 for 5 cans
    number_of_sets = total_cans_to_buy / cans_per_set

    # L4
    cost_per_set = 2 # $2 for 5 cans
    total_juice_cost = cost_per_set * number_of_sets

    # L5
    total_payment = total_ice_cream_cost + total_juice_cost

    # FA
    answer = total_payment
    return answer