def solve():
    """Index: 2270.
    Returns: the percentage of girls in the class who like playing basketball.
    """
    # L1
    percent_total = 100 # WK
    percent_girls = 60 # 60% are girls
    percent_boys = percent_total - percent_girls

    # L2
    total_students = 25 # June’s class has 25 students
    percent_boys_decimal = percent_boys * 0.01 # convert percent to decimal
    num_boys = total_students * percent_boys_decimal

    # L3
    percent_boys_like_basketball = 40 # 40% of the boys like playing basketball
    percent_boys_dont_like_basketball = percent_total - percent_boys_like_basketball

    # L4
    percent_boys_dont_like_basketball_decimal = percent_boys_dont_like_basketball * 0.01
    num_boys_dont_like_basketball = num_boys * percent_boys_dont_like_basketball_decimal

    # L5
    girls_like_basketball_multiplier = 2 # double the number of boys who don't like to
    num_girls_like_basketball = num_boys_dont_like_basketball * girls_like_basketball_multiplier

    # L6
    num_girls = total_students - num_boys

    # L7
    percent_girls_like_basketball = num_girls_like_basketball / num_girls

    # FA
    answer = percent_girls_like_basketball
    return answer