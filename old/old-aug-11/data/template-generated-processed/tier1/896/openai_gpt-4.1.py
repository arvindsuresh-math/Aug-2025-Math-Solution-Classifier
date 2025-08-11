def solve():
    """Index: 896.
    Returns: Kim's total points in the contest.
    """
    # L1
    easy_correct = 6 # Kim got 6 correct answers in the easy
    easy_point = 2 # 2 points for every correct answer in the easy round
    easy_points = easy_correct * easy_point

    # L2
    average_correct = 2 # 2 correct answers in the average
    average_point = 3 # 3 points for every correct answer in the average round
    average_points = average_correct * average_point

    # L3
    hard_correct = 4 # 4 correct answers in the difficult round
    hard_point = 5 # 5 points for every correct answer in the hard round
    hard_points = hard_correct * hard_point

    # L4
    total_points = easy_points + average_points + hard_points

    # FA
    answer = total_points
    return answer