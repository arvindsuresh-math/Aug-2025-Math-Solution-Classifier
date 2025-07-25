def solve():
    """Index: 7173.
    Returns: the number of students who choose to attend Harvard University.
    """
    # L1
    total_applicants = 20000 # 20,000 high school students apply
    acceptance_rate_decimal = 0.05 # 5% of those 20,000 students are accepted
    accepted_students = total_applicants * acceptance_rate_decimal

    # L2
    attendance_rate_decimal = 0.9 # 90% choose to attend the university
    attending_students = accepted_students * attendance_rate_decimal

    # FA
    answer = attending_students
    return answer