def solve():
    """Index: 268.
    Returns: the average number of carnations in the bouquets.
    """
    # L1
    carnations_bouquet1 = 9 # first included 9 carnations
    carnations_bouquet2 = 14 # second included 14 carnations
    carnations_bouquet3 = 13 # third included 13 carnations
    total_carnations = carnations_bouquet1 + carnations_bouquet2 + carnations_bouquet3

    # L2
    number_of_bouquets = 3 # There are 3 bouquets

    # L3
    average_carnations = total_carnations / number_of_bouquets

    # FA
    answer = average_carnations
    return answer