def solve():
    """Index: 2085.
    Returns: the sale price of the NES.
    """
    # L1
    snes_value = 150 # SNES is worth $150
    trade_in_percent = 0.8 # store gives him 80% of that value
    trade_in_value = snes_value * trade_in_percent

    # L2
    cash_given = 80 # He gives $80
    total_spent = trade_in_value + cash_given

    # L3
    change_received = 10 # gets back $10 change
    game_value = 30 # a game worth $30
    total_received = change_received + game_value

    # L4
    nes_sale_price = total_spent - total_received

    # FA
    answer = nes_sale_price
    return answer