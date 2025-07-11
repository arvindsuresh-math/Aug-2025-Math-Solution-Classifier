def solve():
    """Index: 1716.
    Returns: the total rotations of objects made by the winner.
    """
    # L1
    toby_baseballs = 5 # 5 baseballs
    toby_rotations_per_ball = 80 # 80 rotations
    toby_total_rotations = toby_baseballs * toby_rotations_per_ball

    # L2
    friend_apples = 4 # 4 apples
    friend_rotations_per_apple = 101 # 101 rotations
    friend_total_rotations = friend_apples * friend_rotations_per_apple

    # L3
    winner_rotations = max(toby_total_rotations, friend_total_rotations)

    # FA
    answer = winner_rotations
    return answer