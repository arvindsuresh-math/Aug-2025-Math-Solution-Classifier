def solve():
    """Index: 5846.
    Returns: the total weight John will move if he does three triples.
    """
    # L1
    initial_back_squat_weight = 200 # used to back squat 200 kg
    increase_amount = 50 # increased that by 50 kg
    new_back_squat_weight = initial_back_squat_weight + increase_amount

    # L2
    front_squat_ratio = 0.8 # front squat 80% as much
    front_squat_weight = new_back_squat_weight * front_squat_ratio

    # L3
    triple_percentage = 0.9 # 90% of the amount he front squats
    triple_weight = front_squat_weight * triple_percentage

    # L4
    num_triples = 3 # three triples
    total_weight_moved = triple_weight * num_triples

    # FA
    answer = total_weight_moved
    return answer