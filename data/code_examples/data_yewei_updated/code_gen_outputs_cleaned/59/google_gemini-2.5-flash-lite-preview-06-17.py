def solve(
    coins_hour_1: int = 15, # During the first hour, she collected 15 coins.
    coins_hour_2_3: int = 35, # For the next two hours, she collected 35 coins from the fountain.
    coins_hour_4: int = 50, # In the fourth hour, she collected 50 coins from the fountain
    coins_given_to_coworker: int = 15 # she gave 15 of them to her coworker
):
    """Index: 59.
    Returns: the total number of coins Joanne had after the fourth hour.
    """
    #: L1
    coins_hour_2 = coins_hour_2_3 # 35 coins collected in hour two

    #: L2
    coins_hour_3 = coins_hour_2_3 # 35 coins collected in hour three

    #: L3
    total_coins_before_giving = coins_hour_1 + coins_hour_2 + coins_hour_3 + coins_hour_4

    #: L4
    total_coins_after_giving = total_coins_before_giving - coins_given_to_coworker

    answer = total_coins_after_giving # FINAL ANSWER
    return answer