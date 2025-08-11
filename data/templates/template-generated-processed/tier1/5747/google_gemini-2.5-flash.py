def solve():
    """Index: 5747.
    Returns: the total number of jellybeans in the bag.
    """
    # L1
    black_beans = 8 # 8 black beans
    more_green_beans = 2 # 2 more green beans
    green_beans = black_beans + more_green_beans

    # L2
    less_orange_beans = 1 # 1 less orange bean
    orange_beans = green_beans - less_orange_beans

    # L3
    total_jellybeans = black_beans + green_beans + orange_beans

    # FA
    answer = total_jellybeans
    return answer