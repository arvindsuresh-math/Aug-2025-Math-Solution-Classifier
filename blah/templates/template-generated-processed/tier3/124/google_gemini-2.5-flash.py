def solve():
    """Index: 124.
    Returns: the number of feet of yarn used for the second ball.
    """
    # L1
    yarn_for_third_ball = 27 # She used 27 feet of yarn for the third ball
    third_ball_ratio_denominator = 3 # The third ball is three times as large as the first ball
    yarn_for_first_ball = yarn_for_third_ball / third_ball_ratio_denominator

    # L2
    second_ball_ratio_multiplier = 2 # The first ball is half the size of the second ball
    yarn_for_second_ball = yarn_for_first_ball * second_ball_ratio_multiplier

    # FA
    answer = yarn_for_second_ball
    return answer