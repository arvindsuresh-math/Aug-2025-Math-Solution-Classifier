def solve():
    """Index: 5671.
    Returns: the total time in minutes Brooke will take to answer all his homework.
    """
    # L1
    num_math_problems = 15 # 15 math problems
    time_per_math_problem_minutes = 2 # 2 minutes
    total_math_time_minutes = num_math_problems * time_per_math_problem_minutes

    # L2
    num_social_studies_problems = 6 # 6 social studies problems
    time_per_social_studies_problem_seconds = 30 # 30 seconds
    total_social_studies_time_seconds = num_social_studies_problems * time_per_social_studies_problem_seconds

    # L3
    seconds_per_minute = 60 # WK
    total_social_studies_time_minutes = total_social_studies_time_seconds / seconds_per_minute

    # L4
    num_science_problems = 10 # 10 science problems
    time_per_science_problem_minutes = 1.5 # 1.5 minutes
    total_science_time_minutes = num_science_problems * time_per_science_problem_minutes

    # L5
    total_homework_time_minutes = total_math_time_minutes + total_social_studies_time_minutes + total_science_time_minutes

    # FA
    answer = total_homework_time_minutes
    return answer