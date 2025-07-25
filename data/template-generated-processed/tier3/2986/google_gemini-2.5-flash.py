def solve():
    """Index: 2986.
    Returns: the total amount Miley paid.
    """
    # L1
    cellphone_cost = 800 # Each cellphone costs $800
    num_cellphones = 2 # two cellphones
    total_cost_before_discount = cellphone_cost * num_cellphones

    # L2
    discount_percentage = 5 # 5% discount
    percentage_divisor = 100 # WK
    discount_amount = total_cost_before_discount * discount_percentage / percentage_divisor

    # L3
    amount_paid = total_cost_before_discount - discount_amount

    # FA
    answer = amount_paid
    return answer