def solve():
    """Index: 1417.
    Returns: Mario's age.
    """
    # L4
    sum_for_maria_double_age = 6 # derived from the sum of ages (7) and age difference (1) in the question
    coefficient_for_maria_age = 2 # derived from the algebraic setup of ages (x + x) in the question
    maria_age = sum_for_maria_double_age / coefficient_for_maria_age

    # L5
    mario_is_older_by = 1 # Mario is 1 year older than Maria
    mario_age = maria_age + mario_is_older_by

    # FA
    answer = mario_age
    return answer