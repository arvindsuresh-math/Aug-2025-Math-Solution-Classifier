def solve():
    """Index: 7131.
    Returns: the total money Donna made over 7 days.
    """
    # L1
    dog_walking_hourly_rate = 10.00 # $10.00 an hour
    dog_walking_hours_per_morning = 2 # 2 hours every morning
    dog_walking_earnings_per_morning = dog_walking_hourly_rate * dog_walking_hours_per_morning

    # L2
    days_in_week = 7 # Over 7 days
    total_dog_walking_earnings_per_week = days_in_week * dog_walking_earnings_per_morning

    # L3
    card_shop_hourly_rate = 12.50 # $12.50 an hour
    card_shop_hours_per_day = 2 # 2 hours
    card_shop_earnings_per_day = card_shop_hourly_rate * card_shop_hours_per_day

    # L4
    card_shop_days_per_week = 5 # 5 days a week
    total_card_shop_earnings_per_week = card_shop_days_per_week * card_shop_earnings_per_day

    # L5
    babysitting_hours_per_saturday = 4 # guaranteed 4 hours every Saturday
    babysitting_hourly_rate = 10.00 # $10.00 an hour babysitting
    babysitting_earnings_per_saturday = babysitting_hours_per_saturday * babysitting_hourly_rate

    # L6
    total_earnings_per_week = total_dog_walking_earnings_per_week + total_card_shop_earnings_per_week + babysitting_earnings_per_saturday

    # FA
    answer = total_earnings_per_week
    return answer