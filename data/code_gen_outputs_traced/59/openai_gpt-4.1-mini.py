def solve(
    coins_hour_one: int = 15,  # 15 coins collected in hour one
    coins_hour_two: int = 35,  # 35 coins collected in hour two
    coins_hour_three: int = 35,  # 35 coins collected in hour three
    coins_hour_four: int = 50,  # 50 coins collected in hour four
    coins_given_to_coworker: int = 15  # gave 15 coins to her coworker
):
    """Index: 59.
    Returns: the total number of coins Joanne has after the fourth hour.
    """

    #: L5
    total_coins_before_giving = coins_hour_one + coins_hour_two + coins_hour_three + coins_hour_four # eval: 135 = 15 + 35 + 35 + 50

    #: L6
    total_coins_after_giving = total_coins_before_giving - coins_given_to_coworker # eval: 120 = 135 - 15

    #: FA
    answer = total_coins_after_giving # eval: 120 = 120
    return answer # eval: return 120
