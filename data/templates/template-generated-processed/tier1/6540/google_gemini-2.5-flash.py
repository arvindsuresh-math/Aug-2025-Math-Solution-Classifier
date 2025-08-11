def solve():
    """Index: 6540.
    Returns: the total number of toys Annie, Mike, and Tom have.
    """
    # L1
    annie_multiplier = 3 # three times more toys
    mike_toys = 6 # Mike has 6 toys
    annie_more_than_mike = annie_multiplier * mike_toys

    # L2
    annie_total_toys = annie_more_than_mike + mike_toys

    # L3
    tom_more_than_annie = 2 # two less than Tom (implies Tom has 2 more than Annie)
    tom_total_toys = annie_total_toys + tom_more_than_annie

    # L4
    total_toys = mike_toys + annie_total_toys + tom_total_toys

    # FA
    answer = total_toys
    return answer