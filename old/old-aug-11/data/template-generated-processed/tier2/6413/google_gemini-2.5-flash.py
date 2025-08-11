def solve():
    """Index: 6413.
    Returns: the number of students who will pass the course this year.
    """
    # L1
    students_three_years_ago = 200 # 200 students who passed an English course three years ago
    increase_factor = 1.5 # increased by 50% of the previous year's number
    students_two_years_ago = students_three_years_ago * increase_factor

    # L2
    students_last_year = students_two_years_ago * increase_factor

    # L3
    students_this_year = students_last_year * increase_factor

    # FA
    answer = students_this_year
    return answer