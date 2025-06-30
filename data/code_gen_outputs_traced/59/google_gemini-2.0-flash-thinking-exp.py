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

    #: L5
    total_collected_before_giving = coins_hour_1 + coins_per_hour_next_two_hours + coins_per_hour_next_two_hours + coins_fourth_hour # eval: 135 = 15 + 35 + 35 + 50

    #: L6
    coins_after_giving = total_collected_before_giving - coins_given_to_coworker # eval: 120 = 135 - 15

    #: FA
    answer = coins_after_giving # eval: 120 = 120
    return answer # eval: return 120
