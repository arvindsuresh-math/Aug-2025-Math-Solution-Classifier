def solve():
    """Index: 1593.
    Returns: the total number of paperclips Marion has.
    """
    # L1
    initial_paperclips_yun = 20 # Yun had 20 paperclips initially
    lost_paperclips_yun = 12 # lost 12
    yun_current_paperclips = initial_paperclips_yun - lost_paperclips_yun

    # L2
    fraction_denominator = 4 # 1/4 more
    additional_paperclips = 7 # plus 7
    marion_paperclips = yun_current_paperclips / fraction_denominator + additional_paperclips

    # FA
    answer = marion_paperclips
    return answer