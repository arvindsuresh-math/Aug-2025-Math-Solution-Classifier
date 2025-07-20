def solve():
    """Index: 5519.
    Returns: the total money raised from selling all the treats.
    """
    # L1
    students_brownies = 30 # 30 students
    brownies_per_student = 12 # 12 brownies each
    total_brownies = students_brownies * brownies_per_student

    # L2
    students_cookies = 20 # 20 students
    cookies_per_student = 24 # 24 cookies each
    total_cookies = students_cookies * cookies_per_student

    # L3
    students_donuts = 15 # 15 students
    donuts_per_student = 12 # 12 donuts each
    total_donuts = students_donuts * donuts_per_student

    # L4
    total_treats = total_brownies + total_cookies + total_donuts

    # L5
    price_per_treat = 2.00 # $2.00 each
    total_money_raised = total_treats * price_per_treat

    # FA
    answer = total_money_raised
    return answer