from fractions import Fraction

def solve():
    """Index: 3848.
    Returns: the number of coins James sold.
    """
    # L1
    coin_price = 15 # at $15 each
    num_coins_bought = 20 # 20 coins
    original_investment = coin_price * num_coins_bought

    # L2
    increase_fraction = Fraction(2, 3) # increases by 2/3
    increase_per_coin = coin_price * increase_fraction

    # L3
    new_coin_value = coin_price + increase_per_coin

    # L4
    coins_sold = original_investment / new_coin_value

    # FA
    answer = coins_sold
    return answer