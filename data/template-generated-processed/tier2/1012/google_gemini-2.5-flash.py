def solve():
    """Index: 1012.
    Returns: Brian's total commission on the three sales.
    """
    # L1
    house_price_1 = 157000 # sold for $157,000
    house_price_2 = 499000 # sold for $499,000
    house_price_3 = 125000 # sold for $125,000
    total_sales = house_price_1 + house_price_2 + house_price_3

    # L2
    commission_rate_decimal = 0.02 # makes a 2% commission
    total_commission = total_sales * commission_rate_decimal

    # FA
    answer = total_commission
    return answer