def solve():
    """Index: 2113.
    Returns: the number of coins left after the fifth hour.
    """
    # L1
    coins_first_hour = 20 # she puts in 20 coins in the first hour
    coins_second_hour = 30 # she puts in 30 coins during the next two hours
    coins_third_hour = 30 # she puts in 30 coins during the next two hours
    coins_fourth_hour = 40 # she puts in 40 coins during the fourth hour
    coins_by_fourth_hour = coins_first_hour + coins_second_hour + coins_third_hour + coins_fourth_hour

    # L2
    coins_taken_out = 20 # her mother asks to borrow some money so she takes 20 coins out
    coins_after_fifth_hour = coins_by_fourth_hour - coins_taken_out

    # FA
    answer = coins_after_fifth_hour
    return answer