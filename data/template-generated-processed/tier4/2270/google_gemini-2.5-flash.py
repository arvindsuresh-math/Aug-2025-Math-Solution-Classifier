def solve():
    """Index: 2270.
    Returns: the percentage of girls in the class who like playing basketball.
    """
    # L1
    total_percentage = 100 # WK
    girls_percentage = 60 # 60% are girls
    boys_percentage_num = total_percentage - girls_percentage

    # L2
    total_students = 25 # 25 students
    boys_percentage_decimal = 0.4 # the rest are boys (100-60=40%, so 0.4)
    num_boys = total_students * boys_percentage_decimal

    # L3
    boys_like_basketball_percentage = 40 # 40% of the boys like playing basketball
    boys_dont_like_basketball_percentage_num = total_percentage - boys_like_basketball_percentage

    # L4
    boys_dont_like_basketball_percentage_decimal = 0.6 # the rest don't (100-40=60%, so 0.6)
    boys_dont_like_basketball = num_boys * boys_dont_like_basketball_percentage_decimal

    # L5
    girls_like_basketball_multiplier = 2 # double the number of boys who don't like to
    girls_like_basketball = boys_dont_like_basketball * girls_like_basketball_multiplier

    # L6
    num_girls = total_students - num_boys

    # L7
    percentage_girls_like_basketball_decimal = girls_like_basketball / num_girls
    percentage_multiplier = 100 # WK
    final_percentage = percentage_girls_like_basketball_decimal * percentage_multiplier

    # FA
    answer = final_percentage
    return answer