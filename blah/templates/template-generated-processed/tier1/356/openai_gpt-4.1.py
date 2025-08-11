def solve():
    """Index: 356.
    Returns: the total number of points James got in the quiz bowl.
    """
    # L1
    rounds_played = 5 # played a total of five rounds
    questions_per_round = 5 # each consisting of five questions
    questions_missed = 1 # James only missed one question
    correct_answers = rounds_played * questions_per_round - questions_missed

    # L2
    points_per_correct = 2 # 2 points for each correct answer
    points_from_correct = correct_answers * points_per_correct

    # L3
    rounds_with_bonus = rounds_played - questions_missed

    # L4
    bonus_per_round = 4 # awarded an additional 4 point bonus
    total_bonus = rounds_with_bonus * bonus_per_round

    # L5
    answer = points_from_correct + total_bonus
    return answer