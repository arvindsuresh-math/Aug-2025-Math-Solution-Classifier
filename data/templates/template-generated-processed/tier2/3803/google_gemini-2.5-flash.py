def solve():
    """Index: 3803.
    Returns: the total amount Tom paid.
    """
    # L1
    shirts_per_fandom = 5 # 5 t-shirts
    num_fandoms = 4 # 4 favorite fandoms
    total_shirts = shirts_per_fandom * num_fandoms

    # L2
    normal_shirt_cost = 15 # $15 each
    discount_percent = 0.2 # 20% off sale
    discount_per_shirt = normal_shirt_cost * discount_percent

    # L3
    cost_per_shirt_after_discount = normal_shirt_cost - discount_per_shirt

    # L4
    subtotal_cost = total_shirts * cost_per_shirt_after_discount

    # L5
    tax_percent = 0.1 # 10% tax
    tax_amount = subtotal_cost * tax_percent

    # L6
    total_paid = subtotal_cost + tax_amount

    # FA
    answer = total_paid
    return answer