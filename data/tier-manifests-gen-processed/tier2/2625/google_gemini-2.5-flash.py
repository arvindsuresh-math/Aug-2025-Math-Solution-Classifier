def solve():
    """Index: 2625.
    Returns: the number of friends Toby has who are girls.
    """
    # L1
    boys_count = 33 # 33 friends who are boys
    boys_percentage_decimal = 0.55 # 55% of Toby's friends are boys
    total_friends = boys_count / boys_percentage_decimal

    # L2
    total_percentage = 100 # WK
    boys_percentage_num = 55 # 55% of Toby's friends are boys
    girls_percentage_num = total_percentage - boys_percentage_num

    # L3
    girls_percentage_decimal = girls_percentage_num / 100
    girls_count = total_friends * girls_percentage_decimal

    # FA
    answer = girls_count
    return answer