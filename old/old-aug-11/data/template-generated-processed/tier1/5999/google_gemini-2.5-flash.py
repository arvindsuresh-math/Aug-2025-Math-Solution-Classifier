def solve():
    """Index: 5999.
    Returns: the total number of jelly beans.
    """
    # L1
    multiplier_grape = 5 # five times as many grape jelly beans
    vanilla_jelly_beans = 120 # 120 vanilla jelly beans
    five_times_vanilla = multiplier_grape * vanilla_jelly_beans

    # L2
    fifty_more = 50 # fifty more
    grape_jelly_beans = five_times_vanilla + fifty_more

    # L3
    total_jelly_beans = grape_jelly_beans + vanilla_jelly_beans

    # FA
    answer = total_jelly_beans
    return answer