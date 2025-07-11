def solve():
    """Index: 2625.
    Returns: the number of friends Toby has who are girls.
    """
    # L1
    num_boy_friends = 33 # 33 friends who are boys
    percent_boys_decimal = 0.55 # 55% of Toby's friends are boys
    total_friends = num_boy_friends / percent_boys_decimal

    # L2
    percent_total = 100 # WK
    percent_boys = 55 # 55% of Toby's friends are boys
    percent_girls = percent_total - percent_boys

    # L3
    percent_girls_decimal = 0.45 # .45 (from 45%)
    num_girl_friends = total_friends * percent_girls_decimal

    # FA
    answer = num_girl_friends
    return answer