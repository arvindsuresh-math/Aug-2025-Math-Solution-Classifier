def solve():
    """Index: 4864.
    Returns: the total time it will take to knit all the outfits.
    """
    # L1
    hours_per_mitten = 1 # Each mitten takes her about an hour to knit
    mittens_per_pair = 2 # WK
    time_per_pair_mittens = hours_per_mitten * mittens_per_pair

    # L2
    hours_per_sock = 1.5 # A sock takes an hour and a half
    socks_per_pair = 2 # WK
    time_per_pair_socks = hours_per_sock * socks_per_pair

    # L3
    time_per_hat = 2 # a hat in 2 hours
    time_per_scarf = 3 # A scarf takes her 3 hours
    time_per_sweater = 6 # Each sweater takes her 6 hours
    time_per_outfit = time_per_hat + time_per_scarf + time_per_pair_mittens + time_per_pair_socks + time_per_sweater

    # L4
    num_grandchildren = 3 # 3 grandchildren
    total_time = num_grandchildren * time_per_outfit

    # FA
    answer = total_time
    return answer