def solve():
    """Index: 2113.
    Returns: the number of coins left after the fifth hour.
    """
    # L1
    coins_hour1 = 20 # In the first hour she puts in 20 coins
    coins_hour2 = 30 # During the next two hours she puts in 30 coins each time
    coins_hour3 = 30 # During the next two hours she puts in 30 coins each time
    coins_hour4 = 40 # During the fourth hour she puts in 40 coins
    coins_after_fourth_hour = coins_hour1 + coins_hour2 + coins_hour3 + coins_hour4

    # L2
    coins_taken_out = 20 # she takes 20 coins out
    coins_left_after_fifth_hour = coins_after_fourth_hour - coins_taken_out

    # FA
    answer = coins_left_after_fifth_hour
    return answer