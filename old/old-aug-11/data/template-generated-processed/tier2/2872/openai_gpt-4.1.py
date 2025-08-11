def solve():
    """Index: 2872.
    Returns: the number of oatmeal raisin cookies Giorgio will make.
    """
    # L1
    num_students = 40 # 40 students
    oatmeal_percent = 0.1 # 10% of his classmates want oatmeal raisin
    num_oatmeal_students = num_students * oatmeal_percent

    # L2
    cookies_per_student = 2 # 2 cookies per student
    oatmeal_cookies = num_oatmeal_students * cookies_per_student

    # FA
    answer = oatmeal_cookies
    return answer