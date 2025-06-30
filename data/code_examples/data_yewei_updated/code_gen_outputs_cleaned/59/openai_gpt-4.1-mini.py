def solve(
    coins_first_hour: int = 15,  # 15 coins collected in hour one
    coins_next_two_hours: int = 35,  # 35 coins collected in hour two and three each
    coins_fourth_hour: int = 50,  # 50 coins collected in hour four
    coins_given_to_coworker: int = 15  # 15 coins given to coworker
):
    """Index: 59.
    Returns: the total number of coins Joanne has after the fourth hour.
    """
    #: L5
    total_coins_before_giving = coins_first_hour + coins_next_two_hours + coins_next_two_hours + coins_fourth_hour

    #: L6
    total_coins_after_giving = total_coins_before_giving - coins_given_to_coworker

    answer = total_coins_after_giving  # FINAL ANSWER
    return answer