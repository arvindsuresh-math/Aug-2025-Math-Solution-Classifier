def solve(
    first_hour_coins: int = 15,  # 15 coins collected in hour one
    second_hour_coins: int = 35,  # 35 coins collected in hour two
    third_hour_coins: int = 35,  # 35 coins collected in hour three
    fourth_hour_coins: int = 50,  # 50 coins collected in hour four
    coins_given_to_coworker: int = 15  # gave 15 coins to her coworker
):
    """Index: 59.
    Returns: the total number of coins Joanne has after the fourth hour.
    """
    #: L5
    total_coins_collected = first_hour_coins + second_hour_coins + third_hour_coins + fourth_hour_coins

    #: L6
    coins_remaining = total_coins_collected - coins_given_to_coworker

    answer = coins_remaining  # FINAL ANSWER
    return answer