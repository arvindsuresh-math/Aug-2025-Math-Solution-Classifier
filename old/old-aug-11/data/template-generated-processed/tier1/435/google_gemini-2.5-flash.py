def solve():
    """Index: 435.
    Returns: the amount of money Maria must earn to buy the bike.
    """
    # L1
    saved_amount = 120 # saved $120 toward the purchase
    mother_offer = 250 # Her mother offered her $250
    total_money_maria_has = saved_amount + mother_offer

    # L2
    bike_retail_price = 600 # The retail price at the bike shop stands at $600
    money_to_earn = bike_retail_price - total_money_maria_has

    # FA
    answer = money_to_earn
    return answer