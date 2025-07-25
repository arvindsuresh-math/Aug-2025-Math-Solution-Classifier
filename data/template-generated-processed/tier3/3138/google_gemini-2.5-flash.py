def solve():
    """Index: 3138.
    Returns: the total cash Milo gets.
    """
    # L1
    num_grade_2s = 3 # three 2s
    grade_2_value = 2 # three 2s
    num_grade_3s = 4 # four 3s
    grade_3_value = 3 # four 3s
    grade_4_value = 4 # a 4
    grade_5_value = 5 # and a 5
    total_score = (num_grade_2s * grade_2_value) + (num_grade_3s * grade_3_value) + grade_4_value + grade_5_value

    # L2
    num_grade_4s = 1 # a 4
    num_grade_5s = 1 # and a 5
    total_number_of_grades = num_grade_2s + num_grade_3s + num_grade_4s + num_grade_5s

    # L3
    average_grade = total_score / total_number_of_grades

    # L4
    reward_multiplier = 5 # $5 times the average grade
    cash_earned = reward_multiplier * average_grade

    # FA
    answer = cash_earned
    return answer