def solve(
        coins_hour_1: int = 15, # During the first hour, she collected 15 coins
        coins_hour_2_3: int = 35, # For the next two hours, she collected 35 coins
        coins_hour_4: int = 50, # In the fourth hour, she collected 50 coins
        coins_given_to_coworker: int = 15 # she gave 15 of them to her coworker
    ):
    """Index: 59.
    Returns: the total number of coins Joanne had after the fourth hour.
    """
    #: L1
    # coins_collected_hour1 = coins_hour_1 # This is already represented by the argument

    #: L2
    # coins_collected_hour2 = coins_hour_2_3 # This is already represented by the argument

    #: L3
    # coins_collected_hour3 = coins_hour_2_3 # This is already represented by the argument

    #: L4
    # coins_collected_hour4 = coins_hour_4 # This is already represented by the argument

    #: L5
    total_coins_before_giving_away = coins_hour_1 + coins_hour_2_3 + coins_hour_2_3 + coins_hour_4

    #: L6
    coins_after_giving_away = total_coins_before_giving_away - coins_given_to_coworker

    answer = coins_after_giving_away # FINAL ANSWER
    return answer