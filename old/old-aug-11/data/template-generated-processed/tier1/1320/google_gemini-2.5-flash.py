def solve():
    """Index: 1320.
    Returns: the total dollars Shaniqua would make.
    """
    # L1
    num_haircuts = 8 # 8 haircuts
    price_per_haircut = 12 # makes $12
    total_haircut_earnings = num_haircuts * price_per_haircut

    # L2
    num_styles = 5 # 5 styles
    price_per_style = 25 # makes $25
    total_style_earnings = num_styles * price_per_style

    # L3
    total_earned = total_haircut_earnings + total_style_earnings

    # FA
    answer = total_earned
    return answer