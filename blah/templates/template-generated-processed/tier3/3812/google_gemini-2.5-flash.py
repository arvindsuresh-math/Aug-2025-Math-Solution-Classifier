def solve():
    """Index: 3812.
    Returns: the final score from the three throws.
    """
    # L1
    bullseye_points = 50 # One is a bullseye worth 50 points
    half_divisor = 2 # worth half the points of the bullseye
    third_dart_points = bullseye_points / half_divisor

    # L2
    missed_points = 0 # One completely missed the target, so received no points
    total_score = bullseye_points + missed_points + third_dart_points

    # FA
    answer = total_score
    return answer