def solve():
    """Index: 4640.
    Returns: the number of pencils each sibling gets.
    """
    # L1
    colored_pencils = 14 # 14 colored pencils
    black_pencils = 35 # 35 black pencils
    total_pencils = colored_pencils + black_pencils

    # L2
    pencils_to_keep = 10 # keep 10 of them for herself
    pencils_to_share = total_pencils - pencils_to_keep

    # L3
    num_siblings = 3 # three younger siblings
    pencils_per_sibling = pencils_to_share / num_siblings

    # FA
    answer = pencils_per_sibling
    return answer