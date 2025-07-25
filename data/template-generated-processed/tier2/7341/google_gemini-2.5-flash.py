def solve():
    """Index: 7341.
    Returns: the number of more square feet LaKeisha has to mow to earn enough for the book set.
    """
    # L1
    num_lawns_mowed = 3 # three 20 x 15 foot lawns
    lawn_length = 20 # 20 x 15 foot lawns
    lawn_width = 15 # 20 x 15 foot lawns
    total_area_mowed = num_lawns_mowed * lawn_length * lawn_width

    # L2
    charge_per_sq_ft = 0.10 # charges $.10 for every square foot of lawn
    money_earned = total_area_mowed * charge_per_sq_ft

    # L3
    book_set_cost = 150 # The book set costs $150
    money_needed_more = book_set_cost - money_earned

    # L4
    sq_ft_to_mow_more = money_needed_more / charge_per_sq_ft

    # FA
    answer = sq_ft_to_mow_more
    return answer