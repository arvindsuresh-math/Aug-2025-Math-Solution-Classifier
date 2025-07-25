def solve():
    """Index: 4350.
    Returns: four times the number of marbles Cindy has remaining.
    """
    # L1
    num_friends = 4 # four friends
    marbles_per_friend = 80 # 80 marbles each
    marbles_given_away = num_friends * marbles_per_friend

    # L2
    total_marbles_initial = 500 # 500 marbles that Cindy had
    marbles_remaining = total_marbles_initial - marbles_given_away

    # L3
    multiplier = 4 # four times the number
    final_result = marbles_remaining * multiplier

    # FA
    answer = final_result
    return answer