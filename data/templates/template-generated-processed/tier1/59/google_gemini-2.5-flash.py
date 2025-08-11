def solve():
    """Index: 59.
    Returns: the number of coins Joanne had after the fourth hour.
    """
    # L5
    coins_hour_1 = 15 # collected 15 coins
    coins_hour_2 = 35 # collected 35 coins from the fountain
    coins_hour_3 = 35 # collected 35 coins from the fountain
    coins_hour_4 = 50 # collected 50 coins from the fountain
    total_coins_before_giving = coins_hour_1 + coins_hour_2 + coins_hour_3 + coins_hour_4

    # L6
    coins_given_to_coworker = 15 # gave 15 of them to her coworker
    final_coins = total_coins_before_giving - coins_given_to_coworker

    # FA
    answer = final_coins
    return answer