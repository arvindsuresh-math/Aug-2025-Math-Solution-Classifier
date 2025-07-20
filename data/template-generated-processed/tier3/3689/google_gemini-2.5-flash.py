def solve():
    """Index: 3689.
    Returns: the total number of yellow picks in Johnny's collection.
    """
    # L1
    blue_picks_count = 12 # 12 blue picks
    blue_picks_fraction_denominator = 3 # one-third of his picks are blue
    total_picks = blue_picks_fraction_denominator * blue_picks_count

    # L2
    red_picks_fraction_denominator = 2 # Half of his picks are red
    red_picks = total_picks / red_picks_fraction_denominator

    # L3
    yellow_picks = total_picks - red_picks - blue_picks_count

    # FA
    answer = yellow_picks
    return answer