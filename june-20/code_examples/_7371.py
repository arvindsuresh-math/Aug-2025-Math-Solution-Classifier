def solve(
    baseline_bonus: int = 500, # Karen gets a $500 bonus
    baseline_avg_score: int = 75, # if their average score is above 75
    extra_bonus_per_point: int = 10, # plus an extra $10 bonus for every additional point the average score increases above 75
    tests_graded_so_far: int = 8, # So far, Karen has graded 8 tests
    avg_so_far: int = 70, # and the average is 70
    max_score_per_student: int = 150, # each student can have a maximum score of 150
    desired_bonus: int = 600 # Karen wants to earn a $600 bonus
):
    """Index: 7371.
    Returns: the combined score needed in the last two tests to ensure that Karen earns a $600 bonus."""
    #: L1
    extra_bonus_needed = desired_bonus - baseline_bonus

    #: L2
    extra_points_needed = extra_bonus_needed / extra_bonus_per_point

    #: L3
    target_avg_score = baseline_avg_score + extra_points_needed

    #: L4
    total_tests = tests_graded_so_far + 2

    #: L5
    total_points_needed = target_avg_score * total_tests

    #: L6
    points_earned_so_far = avg_so_far * tests_graded_so_far

    #: L7
    points_needed_last_two_tests = total_points_needed - points_earned_so_far

    answer = points_needed_last_two_tests  # FINAL ANSWER
    return answer