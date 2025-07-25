def solve(
        coins_hour_1: int = 15, # During the first hour, she collected 15 coins
        coins_hour_2_3: int = 35, # For the next two hours, she collected 35 coins
        coins_hour_4: int = 50, # In the fourth hour, she collected 50 coins
        coins_given_to_coworker: int = 15 # she gave 15 of them to her coworker
    ):
    """Index: 59.
    Returns: the total number of coins Joanne had after the fourth hour.
    """

    #: L5

    #: L6
    coins_after_giving_away = coins_hour_2_3 - coins_given_to_coworker # eval: 20 = 35 - 15

    #: FA
    answer = coins_after_giving_away
    return answer # eval: return 20
