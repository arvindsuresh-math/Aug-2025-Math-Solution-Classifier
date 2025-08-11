def solve():
    """Index: 896.
    Returns: Kim's total points in the contest.
    """
    # L1
    kim_correct_easy = 6 # 6 correct answers in the easy
    points_per_easy_correct = 2 # 2 points for every correct answer in the easy
    points_easy_round = kim_correct_easy * points_per_easy_correct

    # L2
    kim_correct_average = 2 # 2 correct answers in the average
    points_per_average_correct = 3 # 3 points for every correct answer in the average
    points_average_round = kim_correct_average * points_per_average_correct

    # L3
    kim_correct_hard = 4 # 4 correct answers in the difficult round
    points_per_hard_correct = 5 # 5 points for every correct answer in the hard rounds
    points_hard_round = kim_correct_hard * points_per_hard_correct

    # L4
    total_points = points_easy_round + points_average_round + points_hard_round

    # FA
    answer = total_points
    return answer