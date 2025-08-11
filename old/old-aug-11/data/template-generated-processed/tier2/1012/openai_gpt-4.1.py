def solve():
    """Index: 1012.
    Returns: Brian's total commission on the three sales.
    """
    # L1
    house1_price = 157000 # houses sold for $157,000
    house2_price = 499000 # houses sold for $499,000
    house3_price = 125000 # houses sold for $125,000
    total_sales = house1_price + house2_price + house3_price

    # L2
    commission_rate = 0.02 # 2% commission
    total_commission = total_sales * commission_rate

    # FA
    answer = total_commission
    return answer