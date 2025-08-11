def solve():
    """Index: 4893.
    Returns: the total number of counselors Camp Cedar needs.
    """
    # L1
    boys_count = 40 # 40 boys
    girls_multiplier = 3 # 3 times as many girls
    girls_count = girls_multiplier * boys_count

    # L2
    total_children = boys_count + girls_count

    # L3
    children_per_counselor = 8 # 1 counselor for every 8 children
    counselors_needed = total_children / children_per_counselor

    # FA
    answer = counselors_needed
    return answer