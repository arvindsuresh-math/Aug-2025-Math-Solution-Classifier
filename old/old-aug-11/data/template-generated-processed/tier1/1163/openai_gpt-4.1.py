def solve():
    """Index: 1163.
    Returns: the number of carnations in the third bouquet.
    """
    # L2
    average_carnations = 12 # average number of carnations in the bouquets is 12
    num_bouquets = 3 # three bouquets
    total_carnations = average_carnations * num_bouquets

    # L3
    first_bouquet = 9 # first included 9 carnations
    second_bouquet = 14 # second included 14 carnations
    accounted_for = first_bouquet + second_bouquet

    # L4
    third_bouquet = total_carnations - accounted_for

    # FA
    answer = third_bouquet
    return answer