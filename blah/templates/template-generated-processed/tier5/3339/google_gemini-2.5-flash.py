def solve():
    """Index: 3339.
    Returns: the number of students last year.
    """
    # L3
    students_this_year = 960 # The number of students this year is 960
    increase_percentage = 20 # increased by 20%
    increase_factor = 1 + (increase_percentage / 100)
    students_last_year = students_this_year / increase_factor

    # FA
    answer = students_last_year
    return answer