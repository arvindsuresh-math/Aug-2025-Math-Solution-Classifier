def solve():
    """Index: 2872.
    Returns: the number of oatmeal raisin cookies Giorgio will make.
    """
    # L1
    total_students = 40 # 40 students
    oatmeal_raisin_percent = 0.1 # 10% of his classmates want oatmeal raisin
    students_wanting_oatmeal_raisin = total_students * oatmeal_raisin_percent

    # L2
    cookies_per_student = 2 # 2 cookies per student
    oatmeal_raisin_cookies = students_wanting_oatmeal_raisin * cookies_per_student

    # FA
    answer = oatmeal_raisin_cookies
    return answer