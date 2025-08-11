def solve():
    """Index: 6852.
    Returns: the amount of money saved by buying the cheaper lens.
    """
    # L1
    original_lens_cost = 300 # $300 lens
    discount_rate = 0.2 # 20% discount
    discount_amount = original_lens_cost * discount_rate

    # L2
    discounted_lens_cost = original_lens_cost - discount_amount

    # L3
    cheaper_lens_cost = 220 # $220 lens
    money_saved = discounted_lens_cost - cheaper_lens_cost

    # FA
    answer = money_saved
    return answer