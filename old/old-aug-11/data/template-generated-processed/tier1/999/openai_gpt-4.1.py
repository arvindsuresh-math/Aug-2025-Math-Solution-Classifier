def solve():
    """Index: 999.
    Returns: the amount left in Miss Grayson's class fund after the field trip costs are paid.
    """
    # L1
    student_contribution = 5 # each of her students contributed $5 each
    num_students = 20 # There are 20 students in her class
    total_student_contribution = student_contribution * num_students

    # L2
    initial_fund = 50 # Miss Grayson's class raised $50
    total_fund = total_student_contribution + initial_fund

    # L3
    cost_per_student = 7 # the cost of the trip is $7 for each student
    total_cost = cost_per_student * num_students

    # L4
    fund_left = total_fund - total_cost

    # FA
    answer = fund_left
    return answer