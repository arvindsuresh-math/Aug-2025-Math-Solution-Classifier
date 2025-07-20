def solve():
    """Index: 6935.
    Returns: the total kilowatts consumed by the air conditioner over 5 days.
    """
    # L1
    total_kilowatts_8_hours = 7.2 # 7.2 kilowatts
    initial_hours = 8 # eight hours
    kilowatts_per_hour = total_kilowatts_8_hours / initial_hours

    # L2
    daily_hours = 6 # 6 hours a day
    daily_kilowatts = kilowatts_per_hour * daily_hours

    # L3
    num_days = 5 # for 5 days
    total_consumption_5_days = daily_kilowatts * num_days

    # FA
    answer = total_consumption_5_days
    return answer