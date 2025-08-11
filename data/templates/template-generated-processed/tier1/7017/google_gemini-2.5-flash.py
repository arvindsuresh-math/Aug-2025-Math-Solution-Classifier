def solve():
    """Index: 7017.
    Returns: the profit she will make from selling the rugs.
    """
    # L1
    buy_price_per_rug = 40 # buys handmade rugs at $40 each
    sell_price_per_rug = 60 # sells them at $60 each
    profit_per_rug = sell_price_per_rug - buy_price_per_rug

    # L2
    num_rugs_bought = 20 # bought 20 rugs
    total_profit = num_rugs_bought * profit_per_rug

    # FA
    answer = total_profit
    return answer