def solve():
    """Index: 325.
    Returns: the total number of questions Bob created in three hours.
    """
    # L1
    first_hour = 13 # created 13 questions in the first hour

    # L2
    double = 2 # doubled his rate
    second_hour = first_hour * double

    # L3
    third_hour = second_hour * double

    # L4
    total_questions = first_hour + second_hour + third_hour

    # FA
    answer = total_questions
    return answer