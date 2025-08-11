def solve():
    """Index: 6584.
    Returns: the total amount Eugene has to pay.
    """
    # L1
    num_tshirts = 4 # four T-shirts
    cost_tshirt = 20 # $20 each
    total_cost_tshirts = num_tshirts * cost_tshirt

    # L2
    num_pants = 3 # three pairs of pants
    cost_pants = 80 # $80
    total_cost_pants = num_pants * cost_pants

    # L3
    num_shoes = 2 # two pairs of shoes
    cost_shoes = 150 # $150
    total_cost_shoes = num_shoes * cost_shoes

    # L4
    total_cost_before_discount = total_cost_tshirts + total_cost_pants + total_cost_shoes

    # L5
    discount_percentage = 10 # 10% discount
    discount_divisor = 100 # WK
    discount_amount = (discount_percentage / discount_divisor) * total_cost_before_discount
    final_cost = total_cost_before_discount - discount_amount

    # FA
    answer = final_cost
    return answer