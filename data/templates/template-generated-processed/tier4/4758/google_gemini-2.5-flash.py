def solve():
    """Index: 4758.
    Returns: the amount paying students pay for lunch.
    """
    # L1
    total_percent = 100 # WK
    free_lunch_percent = 40 # 40% of the students receive a free lunch
    paying_students_percent = total_percent - free_lunch_percent

    # L2
    total_students = 50 # 50 students
    paying_students_percent_decimal = paying_students_percent / 100.0
    num_paying_students = total_students * paying_students_percent_decimal

    # L3
    total_cost_to_feed_all = 210 # It costs $210 to feed 50 students
    cost_per_paying_student = total_cost_to_feed_all / num_paying_students

    # FA
    answer = cost_per_paying_student
    return answer