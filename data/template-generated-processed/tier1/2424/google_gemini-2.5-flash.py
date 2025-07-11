def solve():
    """Index: 2424.
    Returns: the number of mistakes Sammy made.
    """
    # L1
    bryan_score = 20 # Bryan's score on a math exam is 20
    jen_more_than_bryan = 10 # Jen scored 10 more than Bryan
    jen_score = bryan_score + jen_more_than_bryan

    # L2
    sammy_fewer_than_jen = 2 # Sammy scored 2 fewer than Jen
    sammy_score = jen_score - sammy_fewer_than_jen

    # L3
    total_exam_points = 35 # the math exam has 35 points in all
    sammy_mistakes = total_exam_points - sammy_score

    # FA
    answer = sammy_mistakes
    return answer