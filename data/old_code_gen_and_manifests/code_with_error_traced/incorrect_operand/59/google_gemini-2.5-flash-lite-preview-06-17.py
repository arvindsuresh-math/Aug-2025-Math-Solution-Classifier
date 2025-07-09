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
    coins_hour_1_total = coins_hour_1 # eval: 15 = 15

    #: L2
    coins_hour_2_total = coins_hour_2_3 # eval: 35 = 35

    #: L3
    coins_hour_3_total = coins_hour_2_3 # eval: 35 = 35

    #: L4
    coins_hour_4_total = coins_hour_4 # eval: 50 = 50

    #: L5
    total_coins_before_giving = coins_hour_2_total + coins_hour_2_total + coins_hour_3_total + coins_hour_4_total # eval: 155 = 35 + 35 + 35 + 50

    #: L6
    total_coins_after_giving = total_coins_before_giving - coins_given_to_coworker # eval: 140 = 155 - 15

    #: FA
    answer = total_coins_after_giving
    return answer # eval: return 140
