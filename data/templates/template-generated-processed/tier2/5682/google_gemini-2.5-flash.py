def solve():
    """Index: 5682.
    Returns: the total commission Enrique earns.
    """
    # L1
    num_suits = 2 # 2 $700.00 suits
    suit_price = 700.00 # $700.00 suits
    total_suit_sales = num_suits * suit_price

    # L2
    num_shirts = 6 # 6 shirts
    shirt_price = 50.00 # $50.00 each
    total_shirt_sales = num_shirts * shirt_price

    # L3
    num_loafers = 2 # 2 pairs of loafers
    loafer_price = 150.00 # $150.00 each
    total_loafer_sales = num_loafers * loafer_price

    # L4
    total_sales = total_suit_sales + total_shirt_sales + total_loafer_sales

    # L5
    commission_rate_percent = 15 # 15% commission
    commission_rate_decimal = 0.15 # .15*2000
    total_commission = commission_rate_decimal * total_sales

    # FA
    answer = total_commission
    return answer