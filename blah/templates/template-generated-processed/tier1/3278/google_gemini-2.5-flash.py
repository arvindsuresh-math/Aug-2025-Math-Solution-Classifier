def solve():
    """Index: 3278.
    Returns: the total number of books Lily got.
    """
    # L1
    mike_gave_lily = 10 # Mike gave 10 books to Lily
    corey_more_than_mike = 15 # Corey gave Lily 15 more than Mike gave
    corey_gave_lily = mike_gave_lily + corey_more_than_mike

    # L2
    total_lily_got = corey_gave_lily + mike_gave_lily

    # FA
    answer = total_lily_got
    return answer