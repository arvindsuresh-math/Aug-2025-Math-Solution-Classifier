def solve():
    """Index: 6473.
    Returns: the number of candies in one packet.
    """
    # L1
    candies_per_weekday = 2 # eats two candies every day from Monday through Friday
    weekdays_count = 5 # WK
    candies_weekdays = candies_per_weekday * weekdays_count

    # L2
    candies_per_weekend_day = 1 # takes one each during the remaining days of the week
    weekend_days_count = 2 # WK
    candies_weekend = candies_per_weekend_day * weekend_days_count

    # L3
    candies_per_week = candies_weekdays + candies_weekend

    # L4
    num_weeks = 3 # it takes him 3 such weeks
    total_candies_consumed = num_weeks * candies_per_week

    # L5
    num_packets = 2 # two packets of candy
    candies_per_packet = total_candies_consumed / num_packets

    # FA
    answer = candies_per_packet
    return answer