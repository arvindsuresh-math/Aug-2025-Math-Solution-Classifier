def solve():
    """Index: 3987.
    Returns: the number of students who identified chess or basketball as their favorite sport.
    """
    # L1
    chess_percentage = 10 # 10% like chess
    basketball_percentage = 40 # 40% said they like basketball
    combined_percentage = chess_percentage + basketball_percentage

    # L2
    total_students = 250 # If 250 students were interviewed
    percentage_divisor = 100 # WK
    students_chess_basketball = total_students * combined_percentage / percentage_divisor

    # FA
    answer = students_chess_basketball
    return answer