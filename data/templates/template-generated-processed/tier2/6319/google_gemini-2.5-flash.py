def solve():
    """Index: 6319.
    Returns: the total amount Jean needs to pay for the pants.
    """
    # L1
    retail_price_each = 45 # normally retail for $45 each
    discount_rate = 0.2 # sale for 20% off
    discount_per_pair = retail_price_each * discount_rate

    # L2
    price_after_discount_each = retail_price_each - discount_per_pair

    # L3
    num_pairs = 10 # buy 10 new pairs of pants
    total_cost_before_tax = price_after_discount_each * num_pairs

    # L4
    tax_rate = 0.1 # paying a 10% tax
    tax_amount = total_cost_before_tax * tax_rate

    # L5
    final_cost = total_cost_before_tax + tax_amount

    # FA
    answer = final_cost
    return answer