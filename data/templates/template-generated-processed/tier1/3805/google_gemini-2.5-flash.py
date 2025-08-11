def solve():
    """Index: 3805.
    Returns: the total money Janet makes.
    """
    # L1
    exterminator_hourly_rate = 70 # $70 an hour for exterminator work
    exterminator_hours = 20 # 20 hours of exterminator work
    exterminator_earnings = exterminator_hourly_rate * exterminator_hours

    # L2
    sculpture_weight_1 = 5 # a 5-pound sculpture
    sculpture_weight_2 = 7 # a 7-pound sculpture
    total_sculpture_pounds = sculpture_weight_1 + sculpture_weight_2

    # L3
    sculpture_price_per_pound = 20 # $20/pound on her ant nest sculptures
    sculpture_earnings = total_sculpture_pounds * sculpture_price_per_pound

    # L4
    total_earnings = sculpture_earnings + exterminator_earnings

    # FA
    answer = total_earnings
    return answer