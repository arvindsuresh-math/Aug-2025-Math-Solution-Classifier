def solve():
    """Index: 1736.
    Returns: the combined number of chocolate bars Mike and Rita got.
    """
    # L1
    total_bars = 12 # box contains 12 bars
    num_people_sharing = 3 # shared equally between Mike, Rita and Anita
    bars_per_person = total_bars / num_people_sharing

    # L2
    combined_bars = bars_per_person + bars_per_person

    # FA
    answer = combined_bars
    return answer