def solve():
    """Index: 2126.
    Returns: the total number of students Adam will teach in 10 years.
    """
    # L1
    students_per_year = 50 # Adam teaches 50 students a year
    years_after_first = 9 # 10 years, but first year is different
    students_in_9_years = students_per_year * years_after_first

    # L2
    students_first_year = 40 # in the first year he only teaches 40 students
    total_students_10_years = students_in_9_years + students_first_year

    # FA
    answer = total_students_10_years
    return answer