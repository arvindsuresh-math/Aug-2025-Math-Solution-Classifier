def solve():
    """Index: 268.
    Returns: the average number of carnations in the bouquets.
    """
    # L1
    first_bouquet_carnations = 9 # The first included 9 carnations
    second_bouquet_carnations = 14 # the second included 14 carnations
    third_bouquet_carnations = 13 # the third included 13 carnations
    total_carnations = first_bouquet_carnations + second_bouquet_carnations + third_bouquet_carnations

    # L3
    number_of_bouquets = 3 # There are 3 bouquets.
    average_carnations = total_carnations / number_of_bouquets

    # FA
    answer = average_carnations
    return answer