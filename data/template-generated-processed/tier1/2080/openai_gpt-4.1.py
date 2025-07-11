def solve():
    """Index: 2080.
    Returns: the total amount the hairstylist earns per week.
    """
    # L1
    price_normal = 5 # $5 for a normal haircut
    num_normal = 5 # 5 normal haircuts per day
    normal_per_day = price_normal * num_normal

    # L2
    price_special = 6 # $6 for a special haircut
    num_special = 3 # 3 special haircuts per day
    special_per_day = price_special * num_special

    # L3
    price_trendy = 8 # $8 for a trendy haircut
    num_trendy = 2 # 2 trendy haircuts per day
    trendy_per_day = price_trendy * num_trendy

    # L4
    total_per_day = normal_per_day + special_per_day + trendy_per_day

    # L5
    days_per_week = 7 # WK
    total_per_week = total_per_day * days_per_week

    # FA
    answer = total_per_week
    return answer