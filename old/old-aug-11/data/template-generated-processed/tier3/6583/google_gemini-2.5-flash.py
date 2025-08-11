def solve():
    """Index: 6583.
    Returns: the total amount paid for the squat rack and barbell.
    """
    # L1
    squat_rack_cost = 2500 # squat rack for $2500
    barbell_cost_divisor = 10 # 1/10 as much
    barbell_cost = squat_rack_cost / barbell_cost_divisor

    # L2
    total_cost = squat_rack_cost + barbell_cost

    # FA
    answer = total_cost
    return answer