def solve():
    """Index: 2080.
    Returns: the total money the hairstylist earns per week.
    """
    # L1
    normal_haircut_price = 5 # $5 for a normal haircut
    num_normal_haircuts_per_day = 5 # cuts 5 normal haircuts
    normal_earnings_per_day = normal_haircut_price * num_normal_haircuts_per_day

    # L2
    special_haircut_price = 6 # $6 for a special haircut
    num_special_haircuts_per_day = 3 # 3 special haircuts
    special_earnings_per_day = special_haircut_price * num_special_haircuts_per_day

    # L3
    trendy_haircut_price = 8 # $8 for a trendy haircut
    num_trendy_haircuts_per_day = 2 # 2 trendy haircuts
    trendy_earnings_per_day = trendy_haircut_price * num_trendy_haircuts_per_day

    # L4
    total_earnings_per_day = normal_earnings_per_day + special_earnings_per_day + trendy_earnings_per_day

    # L5
    days_in_week = 7 # WK
    earnings_per_week = total_earnings_per_day * days_in_week

    # FA
    answer = earnings_per_week
    return answer