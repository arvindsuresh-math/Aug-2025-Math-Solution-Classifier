def solve():
    """Index: 1381.
    Returns: the number of ounces of water Oliver uses for his baths each week.
    """
    # L1
    total_buckets_to_fill = 14 # filled it 14 times
    buckets_removed = 3 # take away 3 buckets
    normal_buckets = total_buckets_to_fill - buckets_removed

    # L2
    bucket_ounces = 120 # bucket that holds 120 ounces
    daily_ounces = normal_buckets * bucket_ounces

    # L3
    days_per_week = 7 # takes every day
    weekly_ounces = days_per_week * daily_ounces

    # FA
    answer = weekly_ounces
    return answer