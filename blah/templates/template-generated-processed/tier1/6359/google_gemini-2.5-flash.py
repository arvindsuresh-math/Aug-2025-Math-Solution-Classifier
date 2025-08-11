def solve():
    """Index: 6359.
    Returns: the total pounds of dumbbells Parker is using.
    """
    # L1
    initial_num_dumbbells = 4 # 4 twenty pounds dumbbells
    dumbbell_weight = 20 # twenty pounds dumbbells
    initial_total_weight = initial_num_dumbbells * dumbbell_weight

    # L2
    added_num_dumbbells = 2 # added two more dumbbells
    added_weight = added_num_dumbbells * dumbbell_weight

    # L3
    total_weight = added_weight + initial_total_weight

    # FA
    answer = total_weight
    return answer