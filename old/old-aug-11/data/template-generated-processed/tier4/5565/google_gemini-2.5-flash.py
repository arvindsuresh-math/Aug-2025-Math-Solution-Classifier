def solve():
    """Index: 5565.
    Returns: the number of Mr. Angstadt's students who are seniors enrolled in Statistics.
    """
    # L1
    total_students = 120 # 120 students throughout the school day
    statistics_divisor = 2 # Half of them are enrolled in Statistics
    students_in_statistics = total_students / statistics_divisor

    # L2
    seniors_percent = 0.90 # 90 percent are seniors
    seniors_in_statistics = students_in_statistics * seniors_percent

    # FA
    answer = seniors_in_statistics
    return answer