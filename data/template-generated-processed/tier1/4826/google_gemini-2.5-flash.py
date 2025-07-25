def solve():
    """Index: 4826.
    Returns: the number of times Tyson scored one point.
    """
    # L1
    points_per_three_score = 3 # three points
    times_three_score = 15 # fifteen times
    points_from_three_score = points_per_three_score * times_three_score

    # L2
    points_per_two_score = 2 # two points
    times_two_score = 12 # twelve times
    points_from_two_score = points_per_two_score * times_two_score

    # L3
    total_score = 75 # in total he scored 75 points
    points_from_one_score = total_score - points_from_three_score - points_from_two_score

    # FA
    answer = points_from_one_score
    return answer