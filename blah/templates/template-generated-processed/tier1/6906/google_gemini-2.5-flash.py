def solve():
    """Index: 6906.
    Returns: the total number of points Homer scored in all tries.
    """
    # L1
    first_try_score = 400 # 400 points on the first try
    fewer_second_try = 70 # 70 points fewer on the second try
    second_try_score = first_try_score - fewer_second_try

    # L2
    total_score_two_tries = first_try_score + second_try_score

    # L3
    multiplier_third_try = 2 # twice the number of points
    third_try_score = multiplier_third_try * second_try_score

    # L4
    total_score_all_tries = third_try_score + total_score_two_tries

    # FA
    answer = total_score_all_tries
    return answer