def solve():
    """Index: 5231.
    Returns: Jackson's final grade.
    """
    # L1
    hours_gaming = 9 # 9 hours playing video games
    study_divisor = 3 # 1/3 that much time studying
    hours_studying = hours_gaming / study_divisor

    # L2
    points_per_hour_studying = 15 # increases by 15 points for every hour he spends studying
    jacksons_grade = hours_studying * points_per_hour_studying

    # FA
    answer = jacksons_grade
    return answer