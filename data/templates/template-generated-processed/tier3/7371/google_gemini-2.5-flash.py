def solve():
    """Index: 7371.
    Returns: the combined score the last two tests need to have.
    """
    # L1
    goal_bonus = 600 # earn a $600 bonus
    baseline_bonus = 500 # gets a $500 bonus
    extra_bonus_needed = goal_bonus - baseline_bonus

    # L2
    bonus_per_point = 10 # an extra $10 bonus for every additional point
    points_above_baseline = extra_bonus_needed / bonus_per_point

    # L3
    baseline_average_score = 75 # average score is above 75
    target_average_score = points_above_baseline + baseline_average_score

    # L4
    graded_tests = 8 # graded 8 tests
    ungraded_tests = 2 # last two tests
    total_tests = ungraded_tests + graded_tests

    # L5
    total_points_needed = target_average_score * total_tests

    # L6
    current_average = 70 # the average is 70
    current_total_points = current_average * graded_tests

    # L7
    combined_score_needed = total_points_needed - current_total_points

    # FA
    answer = combined_score_needed
    return answer