def solve():
    """Index: 7055.
    Returns: how many more marbles Lisa has than Cindy now.
    """
    # L1
    cindy_initial_marbles = 20 # Cindy had 20 marbles
    cindy_more_than_lisa = 5 # 5 more than what Lisa had
    lisa_initial_marbles = cindy_initial_marbles - cindy_more_than_lisa

    # L2
    marbles_cindy_gave = 12 # Cindy gave her 12 marbles
    cindy_marbles_after_giving = cindy_initial_marbles - marbles_cindy_gave

    # L3
    lisa_marbles_after_receiving = lisa_initial_marbles + marbles_cindy_gave

    # L4
    lisa_more_than_cindy_now = lisa_marbles_after_receiving - cindy_marbles_after_giving

    # FA
    answer = lisa_more_than_cindy_now
    return answer