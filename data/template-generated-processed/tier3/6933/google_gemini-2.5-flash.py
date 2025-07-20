def solve():
    """Index: 6933.
    Returns: the number of cottage pies made.
    """
    # L1
    num_lasagnas = 100 # 100 lasagnas
    mince_per_lasagna = 2 # 2 pounds of ground mince each
    mince_for_lasagnas = num_lasagnas * mince_per_lasagna

    # L2
    total_mince_used = 500 # 500 pounds of ground mince in total
    mince_for_cottage_pies = total_mince_used - mince_for_lasagnas

    # L3
    mince_per_cottage_pie = 3 # 3 pounds of ground mince each
    num_cottage_pies = mince_for_cottage_pies / mince_per_cottage_pie

    # FA
    answer = num_cottage_pies
    return answer