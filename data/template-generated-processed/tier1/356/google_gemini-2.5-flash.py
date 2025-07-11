def solve():
    """Index: 356.
    Returns: the total points James got.
    """
    # L1
    total_rounds = 5 # total of five rounds
    questions_per_round = 5 # five questions
    questions_missed = 1 # only missed one question
    correct_answers_total = total_rounds * questions_per_round - questions_missed

    # L2
    points_per_correct_answer = 2 # 2 points for each correct answer
    points_from_correct_answers = correct_answers_total * points_per_correct_answer

    # L3
    rounds_disqualified_from_bonus = 1 # missing one question would only disqualify him from receiving a bonus in one round
    rounds_with_bonus = total_rounds - rounds_disqualified_from_bonus

    # L4
    bonus_points_per_round = 4 # additional 4 point bonus
    total_bonus_points = rounds_with_bonus * bonus_points_per_round

    # L5
    total_score = points_from_correct_answers + total_bonus_points

    # FA
    answer = total_score
    return answer