def solve():
    """Index: 3891.
    Returns: the number of red jellybeans in the jar.
    """
    # L1
    blue_jellybeans = 14 # 14 blue jellybeans
    purple_jellybeans = 26 # 26 purple jellybeans
    orange_jellybeans = 40 # 40 orange jellybeans
    sum_other_colors = blue_jellybeans + purple_jellybeans + orange_jellybeans

    # L2
    total_jellybeans = 200 # 200 jellybeans in the jar
    red_jellybeans = total_jellybeans - sum_other_colors

    # FA
    answer = red_jellybeans
    return answer