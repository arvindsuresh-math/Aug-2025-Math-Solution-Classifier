def solve():
    """Index: 5397.
    Returns: the total money Grant made from selling his baseball gear.
    """
    # L1
    glove_original_price = 30 # $30 baseball glove
    discount_percent_decimal = 0.20 # at 20% off
    glove_discount_amount = glove_original_price * discount_percent_decimal

    # L2
    glove_final_price = glove_original_price - glove_discount_amount

    # L3
    num_cleats_pairs = 2 # both pair
    price_per_cleat_pair = 10 # $10 each
    cleats_total_price = num_cleats_pairs * price_per_cleat_pair

    # L4
    cards_price = 25 # baseball cards for $25
    bat_price = 10 # $10 for his baseball bat
    total_money_made = cards_price + bat_price + glove_final_price + cleats_total_price

    # FA
    answer = total_money_made
    return answer