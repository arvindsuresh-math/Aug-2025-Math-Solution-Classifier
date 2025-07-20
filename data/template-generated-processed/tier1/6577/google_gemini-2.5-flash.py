def solve():
    """Index: 6577.
    Returns: how many more points Jimmy can lose and still pass the class.
    """
    # L1
    points_per_exam = 20 # 20 points for each of the 3 exams
    num_exams = 3 # 3 exams he wrote
    points_from_exams = points_per_exam * num_exams

    # L2
    points_lost_behavior = 5 # lost 5 points during the school year for bad behavior
    points_after_loss = points_from_exams - points_lost_behavior

    # L3
    points_to_pass = 50 # needs to score at least 50 points to pass
    additional_points_can_lose = points_after_loss - points_to_pass

    # FA
    answer = additional_points_can_lose
    return answer