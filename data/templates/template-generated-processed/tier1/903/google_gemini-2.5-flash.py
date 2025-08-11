def solve():
    """Index: 903.
    Returns: the total amount of money Margaux will collect after 7 days.
    """
    # L1
    friend_daily_pay = 5 # $5 per day
    num_days = 7 # 7 days
    friend_total_pay = friend_daily_pay * num_days

    # L2
    brother_daily_pay = 8 # $8 per day
    brother_total_pay = brother_daily_pay * num_days

    # L3
    cousin_daily_pay = 4 # $4 per day
    cousin_total_pay = cousin_daily_pay * num_days

    # L4
    total_collected = friend_total_pay + brother_total_pay + cousin_total_pay

    # FA
    answer = total_collected
    return answer