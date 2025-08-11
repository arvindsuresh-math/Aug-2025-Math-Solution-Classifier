def solve():
    """Index: 159.
    Returns: the amount Mario would have paid for a haircut on Sunday.
    """
    # L1
    monday_price = 18 # Mario paid $18 for his last haircut on Monday
    weekend_increase_percent_num = 50 # 50% more expensive during the weekends
    percent_factor = 0.01 # WK
    weekend_increase_amount = monday_price * weekend_increase_percent_num * percent_factor

    # L2
    sunday_price = weekend_increase_amount + monday_price

    # FA
    answer = sunday_price
    return answer