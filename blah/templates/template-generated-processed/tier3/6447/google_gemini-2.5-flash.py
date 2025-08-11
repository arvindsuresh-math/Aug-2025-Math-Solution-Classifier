def solve():
    """Index: 6447.
    Returns: the total number of apples Emmy and Gerry can buy.
    """
    # L1
    emmy_money = 200 # Emmy has $200
    gerry_money = 100 # Gerry has $100
    total_money = emmy_money + gerry_money

    # L2
    apple_price = 2 # apples for $2 each
    total_apples = total_money / apple_price

    # FA
    answer = total_apples
    return answer