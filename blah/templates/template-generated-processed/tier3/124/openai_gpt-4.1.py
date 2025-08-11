def solve():
    """Index: 124.
    Returns: the number of feet of yarn used for the second ball.
    """
    # L1
    third_ball_yarn = 27 # She used 27 feet of yarn for the third ball
    first_ball_fraction_of_third = 3 # The first ball is a third of the size of the third ball
    first_ball_yarn = third_ball_yarn / first_ball_fraction_of_third

    # L2
    second_ball_multiple_of_first = 2 # The second ball is twice the size of the first ball
    second_ball_yarn = first_ball_yarn * second_ball_multiple_of_first

    # FA
    answer = second_ball_yarn
    return answer