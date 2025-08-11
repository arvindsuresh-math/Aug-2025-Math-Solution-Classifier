def solve():
    """Index: 6533.
    Returns: the amount of water Tony drank two days ago.
    """
    # L1
    total_percent = 100 # WK
    yesterday_less_percent = 4 # 4% less than what he drank two days ago
    yesterday_percentage = total_percent - yesterday_less_percent

    # L2
    yesterday_ounces = 48 # 48 ounces of water
    one_percent_value = 1 # WK
    ounces_per_percent = yesterday_ounces / yesterday_percentage

    # L3
    total_percent_drank_two_days_ago = 100 # WK
    two_days_ago_ounces = ounces_per_percent * total_percent_drank_two_days_ago

    # FA
    answer = two_days_ago_ounces
    return answer