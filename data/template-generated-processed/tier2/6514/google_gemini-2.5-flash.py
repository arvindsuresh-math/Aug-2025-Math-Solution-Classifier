def solve():
    """Index: 6514.
    Returns: the number of juniors involved in sports.
    """
    # L1
    total_students = 500 # 500 students in a local high school
    junior_percent_decimal = 0.40 # 40 percent are juniors
    num_juniors = total_students * junior_percent_decimal

    # L2
    sports_percent_decimal = 0.70 # 70 percent of juniors are involved in sports
    juniors_in_sports = num_juniors * sports_percent_decimal

    # FA
    answer = juniors_in_sports
    return answer