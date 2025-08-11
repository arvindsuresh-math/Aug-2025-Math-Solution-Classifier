def solve():
    """Index: 6745.
    Returns: the number of balloons each friend has now.
    """
    # L1
    total_balloons = 250 # 250 balloons in one package
    num_friends = 5 # among his 5 friends
    balloons_per_friend_initial = total_balloons / num_friends

    # L2
    balloons_taken_back = 11 # give him 11 balloons
    balloons_per_friend_final = balloons_per_friend_initial - balloons_taken_back

    # FA
    answer = balloons_per_friend_final
    return answer