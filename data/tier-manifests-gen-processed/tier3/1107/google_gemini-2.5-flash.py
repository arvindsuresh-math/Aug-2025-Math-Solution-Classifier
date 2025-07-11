def solve():
    """Index: 1107.
    Returns: the number of gold coins Roman has left.
    """
    # L1
    payment_for_coins = 12 # Dorothy paid $12 for 3 gold coins
    coins_sold_in_L1 = 3 # He sells 3 gold coins to Dorothy
    value_per_gold_coin = payment_for_coins / coins_sold_in_L1

    # L2
    initial_gold_value = 20 # Roman the Tavernmaster has $20 worth of gold coins
    initial_number_of_gold_coins = initial_gold_value / value_per_gold_coin

    # L3
    coins_given_to_dorothy = 3 # He sells 3 gold coins to Dorothy
    remaining_gold_coins = initial_number_of_gold_coins - coins_given_to_dorothy

    # FA
    answer = remaining_gold_coins
    return answer