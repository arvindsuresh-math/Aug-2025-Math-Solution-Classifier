def solve(
    coins_hour_1: int = 15, # During the first hour, she collected 15 coins
    hours_next: int = 2, # For the next two hours
    coins_per_hour_next_two_hours: int = 35, # she collected 35 coins from the fountain
    hour_fourth: int = 4, # In the fourth hour
    coins_fourth_hour: int = 50, # she collected 50 coins from the fountain
    coins_given_to_coworker: int = 15 # she gave 15 of them to her coworker
):
    """Index: 59.
    Returns: the number of coins Joanne had after the fourth hour.
    """
    #: L1
    # 15 coins collected in hour one (already in coins_hour_1)

    #: L2
    # 35 coins collected in hour two (already in coins_per_hour_next_two_hours)

    #: L3
    # 35 coins collected in hour three (already in coins_per_hour_next_two_hours)

    #: L4
    # 50 coins collected in hour four (already in coins_fourth_hour)

    #: L5
    total_collected_before_giving = coins_hour_1 + coins_per_hour_next_two_hours + coins_per_hour_next_two_hours + coins_fourth_hour

    #: L6
    coins_after_giving = total_collected_before_giving - coins_given_to_coworker

    answer = coins_after_giving # FINAL ANSWER
    return answer