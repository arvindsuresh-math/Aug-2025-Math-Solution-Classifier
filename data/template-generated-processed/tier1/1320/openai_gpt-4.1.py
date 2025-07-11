def solve():
    """Index: 1320.
    Returns: the total amount of money Shaniqua would make for 8 haircuts and 5 styles.
    """
    # L1
    num_haircuts = 8 # gave 8 haircuts
    haircut_price = 12 # for every haircut she makes $12
    haircut_earnings = num_haircuts * haircut_price

    # L2
    num_styles = 5 # 5 styles
    style_price = 25 # for every style she makes $25
    style_earnings = num_styles * style_price

    # L3
    total_earned = haircut_earnings + style_earnings

    # FA
    answer = total_earned
    return answer