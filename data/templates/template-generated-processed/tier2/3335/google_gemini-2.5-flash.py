def solve():
    """Index: 3335.
    Returns: the score Margaret received on her test.
    """
    # L1
    average_score = 90 # The average score on last week's Spanish test was 90
    marco_discount_percent_decimal = 0.10 # 10% less
    marco_points_lower = average_score * marco_discount_percent_decimal

    # L2
    marco_score = average_score - marco_points_lower

    # L3
    margaret_extra_points = 5 # Margaret received 5 more points
    margaret_score = margaret_extra_points + marco_score

    # FA
    answer = margaret_score
    return answer