def solve():
    """Index: 1163.
    Returns: the number of carnations in the third bouquet.
    """
    # L2
    average_carnations = 12 # average number of carnations in the bouquets is 12
    num_bouquets = 3 # three bouquets
    total_carnations = average_carnations * num_bouquets

    # L3
    first_bouquet_carnations = 9 # The first included 9 carnations
    second_bouquet_carnations = 14 # the second included 14 carnations
    accounted_for_carnations = first_bouquet_carnations + second_bouquet_carnations

    # L4
    third_bouquet_carnations = total_carnations - accounted_for_carnations

    # FA
    answer = third_bouquet_carnations
    return answer