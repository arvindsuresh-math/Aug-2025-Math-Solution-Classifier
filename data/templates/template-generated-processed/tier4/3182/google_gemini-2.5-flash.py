def solve():
    """Index: 3182.
    Returns: the total amount of money Teagan will pay for shirts and leather jackets.
    """
    # L1
    shirt_original_price = 60 # the price of a shirt in the store was $60
    discount_percentage_num = 20 # reduced the prices of items in her store by 20%
    percent_divisor = 100 # WK
    shirt_discount_amount = shirt_original_price * discount_percentage_num / percent_divisor

    # L2
    shirt_reduced_price = shirt_original_price - shirt_discount_amount

    # L3
    num_shirts = 5 # buying 5 shirts
    total_cost_shirts = shirt_reduced_price * num_shirts

    # L4
    jacket_original_price = 90 # the price of the leather jacket was $90
    discount_factor = 0.2 # reduced the prices of items in her store by 20%
    jacket_discount_amount = jacket_original_price * discount_factor

    # L5
    jacket_reduced_price = jacket_original_price - jacket_discount_amount

    # L6
    num_jackets = 10 # buying 10 leather jackets
    total_cost_jackets = jacket_reduced_price * num_jackets

    # L7
    total_money_paid = total_cost_jackets + total_cost_shirts

    # FA
    answer = total_money_paid
    return answer