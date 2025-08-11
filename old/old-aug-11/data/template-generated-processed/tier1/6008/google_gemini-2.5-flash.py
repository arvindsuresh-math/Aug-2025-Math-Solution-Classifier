def solve():
    """Index: 6008.
    Returns: the total money Tom makes per week.
    """
    # L1
    num_crab_buckets = 8 # 8 crab buckets
    crabs_per_bucket = 12 # 12 crabs
    crabs_per_day = num_crab_buckets * crabs_per_bucket

    # L2
    price_per_crab = 5 # $5 each
    money_per_day = crabs_per_day * price_per_crab

    # L3
    days_per_week = 7 # WK
    money_per_week = days_per_week * money_per_day

    # FA
    answer = money_per_week
    return answer