def solve():
    """Index: 2069.
    Returns: the number of pairs of shoes Page has now.
    """
    # L1
    percent_donated_num = 30 # donates 30%
    percent_donated_decimal = 0.30 # that's .30*80
    percent_factor = 0.01 # WK
    initial_pairs = 80 # has 80 pairs in her closet
    pairs_donated = percent_donated_num * percent_factor * initial_pairs

    # L2
    pairs_after_donation = initial_pairs - pairs_donated

    # L3
    pairs_bought = 6 # buys 6 more pairs
    final_pairs = pairs_after_donation + pairs_bought

    # FA
    answer = final_pairs
    return answer