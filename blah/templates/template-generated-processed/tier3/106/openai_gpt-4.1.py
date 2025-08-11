def solve():
    """Index: 106.
    Returns: the total number of uncommon cards John got.
    """
    # L1
    cards_per_pack = 20 # Each pack has 20 cards
    uncommon_denominator = 4 # 1/4 of those cards are uncommon
    uncommons_per_pack = cards_per_pack / uncommon_denominator

    # L2
    num_packs = 10 # John buys 10 packs
    total_uncommons = num_packs * uncommons_per_pack

    # FA
    answer = total_uncommons
    return answer