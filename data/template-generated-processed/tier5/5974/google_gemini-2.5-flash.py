def solve():
    """Index: 5974.
    Returns: the number of drunk drivers.
    """
    # Define initial question inputs that are used in later computations.
    total_students = 45 # 45 students total
    multiplier_for_speeders = 7 # 7 times that many speeders
    less_than_multiplier = 3 # 3 less than 7 times

    # L1, L2, L3 are algebraic setup and manipulation steps without explicit numerical computations.
    # The problem sets up two equations:
    # 1. d + s = total_students
    # 2. s = multiplier_for_speeders * d - less_than_multiplier
    # Substituting (2) into (1) gives: d + (multiplier_for_speeders * d - less_than_multiplier) = total_students
    # Combining like terms (d + 7d) gives: (1 + multiplier_for_speeders) * d - less_than_multiplier = total_students
    # Which simplifies to: 8d - 3 = 45

    # L4
    # To isolate the term with 'd', we add 'less_than_multiplier' to 'total_students'.
    # The solution text states 'Adding 4 to both sides', but the actual value added to 45 to get 48 is 3 (from 8d - 3 = 45).
    right_side_after_addition = total_students + less_than_multiplier

    # L5
    # The coefficient of 'd' is (1 + multiplier_for_speeders).
    coefficient_d_combined = 1 + multiplier_for_speeders
    num_drunk_drivers = right_side_after_addition / coefficient_d_combined

    # FA
    answer = num_drunk_drivers
    return answer