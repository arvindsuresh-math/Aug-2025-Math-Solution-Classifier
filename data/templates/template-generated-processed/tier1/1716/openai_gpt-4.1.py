def solve():
    """Index: 1716.
    Returns: the total rotations of objects made by the winner.
    """
    # L1
    toby_balls = 5 # Toby has 5 baseballs
    toby_rotations_per_ball = 80 # each one makes 80 rotations
    toby_total_rotations = toby_balls * toby_rotations_per_ball

    # L2
    friend_apples = 4 # His friend has 4 apples
    friend_rotations_per_apple = 101 # each one makes 101 rotations
    friend_total_rotations = friend_apples * friend_rotations_per_apple

    # L3
    winner_rotations = friend_total_rotations if friend_total_rotations > toby_total_rotations else toby_total_rotations

    # FA
    answer = winner_rotations
    return answer