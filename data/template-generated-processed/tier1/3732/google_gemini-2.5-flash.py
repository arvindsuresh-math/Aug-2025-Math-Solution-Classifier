def solve():
    """Index: 3732.
    Returns: the number of minutes David spent reading.
    """
    # L1
    math_minutes = 15 # 15 minutes on his math homework
    spelling_minutes = 18 # 18 minutes on his spelling homework
    homework_minutes = math_minutes + spelling_minutes

    # L2
    total_homework_time = 60 # finished his homework in 60 minutes
    reading_minutes = total_homework_time - homework_minutes

    # FA
    answer = reading_minutes
    return answer