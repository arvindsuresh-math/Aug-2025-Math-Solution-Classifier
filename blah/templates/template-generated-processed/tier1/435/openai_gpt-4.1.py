def solve():
    """Index: 435.
    Returns: the amount of money Maria must earn to buy the bike.
    """
    # L1
    maria_saved = 120 # She saved $120 toward the purchase
    mother_gave = 250 # her mother offered her $250
    maria_total = maria_saved + mother_gave

    # L2
    bike_price = 600 # The retail price at the bike shop stands at $600
    maria_needs = bike_price - maria_total

    # FA
    answer = maria_needs
    return answer