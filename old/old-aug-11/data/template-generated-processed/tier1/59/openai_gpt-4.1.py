def solve():
    """Index: 59.
    Returns: the number of coins Joanne had after the fourth hour.
    """
    # L5
    coins_hour1 = 15 # she collected 15 coins (first hour)
    coins_hour2 = 35 # she collected 35 coins (second hour)
    coins_hour3 = 35 # she collected 35 coins (third hour)
    coins_hour4 = 50 # she collected 50 coins (fourth hour)
    total_before_giving = coins_hour1 + coins_hour2 + coins_hour3 + coins_hour4

    # L6
    coins_given = 15 # she gave 15 of them to her coworker
    coins_after_giving = total_before_giving - coins_given

    # FA
    answer = coins_after_giving
    return answer