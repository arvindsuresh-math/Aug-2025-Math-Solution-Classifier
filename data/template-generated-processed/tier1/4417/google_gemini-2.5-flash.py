def solve():
    """Index: 4417.
    Returns: the number of additional times Levi needs to score to reach his goal.
    """
    # L1
    brother_initial_score = 12 # his brother had scored 12 times
    brother_additional_score = 3 # his brother scores another 3 times
    brother_total_score = brother_initial_score + brother_additional_score

    # L2
    target_difference = 5 # beat his brother by at least 5 baskets
    levi_target_score = brother_total_score + target_difference

    # L3
    levi_initial_score = 8 # Levi had scored 8 times
    levi_additional_scores_needed = levi_target_score - levi_initial_score

    # FA
    answer = levi_additional_scores_needed
    return answer