def solve():
    """Index: 2768.
    Returns: the total number of balls Robert has now.
    """
    # L1
    tim_total_balls = 40 # his 40 balls
    half_divisor = 2 # half of his 40 balls
    balls_from_tim = tim_total_balls / half_divisor

    # L2
    robert_initial_balls = 25 # Robert had 25 balls
    robert_total_balls = robert_initial_balls + balls_from_tim

    # FA
    answer = robert_total_balls
    return answer