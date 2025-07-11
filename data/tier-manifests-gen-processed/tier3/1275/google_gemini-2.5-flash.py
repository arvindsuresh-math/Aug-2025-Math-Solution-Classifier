def solve():
    """Index: 1275.
    Returns: the total number of straws Ginger needs.
    """
    # L1
    orange_straws_per_mat = 30 # 30 orange straws
    green_straw_divisor = 2 # half as many green straws as orange straws
    green_straws_per_mat = orange_straws_per_mat / green_straw_divisor

    # L2
    red_straws_per_mat = 20 # 20 red straws
    total_straws_per_mat = green_straws_per_mat + red_straws_per_mat + orange_straws_per_mat

    # L3
    number_of_mats = 10 # make 10 mats
    total_straws_needed = total_straws_per_mat * number_of_mats

    # FA
    answer = total_straws_needed
    return answer