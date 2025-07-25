def solve():
    """Index: 1381.
    Returns: the amount of water Oliver uses each week for his baths in ounces.
    """
    # L1
    total_buckets_to_fill = 14 # filled it 14 times
    buckets_to_take_away = 3 # take away 3 buckets
    normal_buckets_used = total_buckets_to_fill - buckets_to_take_away

    # L2
    bucket_capacity_ounces = 120 # bucket that holds 120 ounces
    ounces_per_day = normal_buckets_used * bucket_capacity_ounces

    # L3
    days_in_week = 7 # WK
    ounces_per_week = days_in_week * ounces_per_day

    # FA
    answer = ounces_per_week
    return answer