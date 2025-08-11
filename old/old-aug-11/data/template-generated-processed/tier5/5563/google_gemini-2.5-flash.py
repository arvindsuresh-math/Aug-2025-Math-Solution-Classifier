def solve():
    """Index: 5563.
    Returns: the number of littering citations issued.
    """
    # L2
    littering_off_leash_factor = 2 # issued the same number for littering as he did for off-leash dogs
    parking_fine_multiplier = 2 # double the number of other citations
    total_parking_fine_factor = parking_fine_multiplier * littering_off_leash_factor

    # L3
    total_citations_issued = 24 # issued 24 citations over the past three hours
    total_citations_sum_coefficient = littering_off_leash_factor + total_parking_fine_factor

    # L4
    littering_citations = total_citations_issued / total_citations_sum_coefficient

    # FA
    answer = littering_citations
    return answer