def solve():
    """Index: 3206.
    Returns: the total money the company will earn.
    """
    # L1
    days_in_week = 7 # WK

    # L2
    computers_per_day = 1500 # 1500 computers per day
    computers_per_week = computers_per_day * days_in_week

    # L3
    price_per_computer = 150 # $150
    total_earnings = computers_per_week * price_per_computer

    # FA
    answer = total_earnings
    return answer