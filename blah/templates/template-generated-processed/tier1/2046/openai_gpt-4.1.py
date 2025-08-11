def solve():
    """Index: 2046.
    Returns: the total number of coins four bank tellers have in all.
    """
    # L1
    rolls_per_teller = 10 # Each bank teller has 10 rolls of coins
    coins_per_roll = 25 # Each roll has 25 coins
    coins_per_teller = rolls_per_teller * coins_per_roll

    # L2
    num_tellers = 4 # four bank tellers
    total_coins = coins_per_teller * num_tellers

    # FA
    answer = total_coins
    return answer