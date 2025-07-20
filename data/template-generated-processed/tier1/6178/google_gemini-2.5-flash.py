def solve():
    """Index: 6178.
    Returns: the amount of money Ibrahim lacks.
    """
    # L1
    mp3_player_price = 120 # an MP3 player for 120 euros
    cd_price = 19 # a CD for 19 euros
    total_purchase_price = mp3_player_price + cd_price

    # L2
    savings = 55 # 55 euros in savings
    father_contribution = 20 # giving him 20 euros
    total_money_has = savings + father_contribution

    # L3
    money_lacks = total_purchase_price - total_money_has

    # FA
    answer = money_lacks
    return answer