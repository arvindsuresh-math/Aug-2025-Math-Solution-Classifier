def solve():
    """Index: 4030.
    Returns: the number of rubber bands Ylona had in the beginning.
    """
    # L1
    band_given_to_justine = 2 # give two bands each to Justine
    band_given_to_ylona = 2 # give two bands each to Ylona
    bailey_gave_total = band_given_to_justine + band_given_to_ylona

    # L2
    bailey_left_with = 8 # left with only 8 rubber bands
    bailey_initial = bailey_left_with + bailey_gave_total

    # L3
    justine_more_than_bailey = 10 # 10 more rubber bands than Bailey
    justine_initial = bailey_initial + justine_more_than_bailey

    # L4
    ylona_more_than_justine = 2 # 2 fewer bands than Ylona
    ylona_initial = justine_initial + ylona_more_than_justine

    # FA
    answer = ylona_initial
    return answer