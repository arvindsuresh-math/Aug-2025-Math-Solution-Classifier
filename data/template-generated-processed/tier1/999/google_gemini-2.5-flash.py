def solve():
    """Index: 999.
    Returns: the amount of money left in Miss Grayson's class fund.
    """
    # L1
    student_contribution_per_student = 5 # contributed $5 each
    num_students = 20 # 20 students in her class
    total_student_contribution = student_contribution_per_student * num_students

    # L2
    initial_class_fund = 50 # raised $50 for their field trip
    total_funds_available = total_student_contribution + initial_class_fund

    # L3
    cost_per_student = 7 # cost of the trip is $7 for each student
    total_trip_cost = cost_per_student * num_students

    # L4
    remaining_fund = total_funds_available - total_trip_cost

    # FA
    answer = remaining_fund
    return answer