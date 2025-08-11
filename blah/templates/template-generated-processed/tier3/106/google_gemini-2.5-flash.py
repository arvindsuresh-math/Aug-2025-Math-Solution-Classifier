def solve():
    """Index: 106.
    Returns: the total number of uncommon cards John got.
    """
    # L1
    cards_per_pack = 20 # Each pack has 20 cards
    uncommon_fraction_denominator = 4 # 1/4 of those cards are uncommon
    uncommon_cards_per_pack = cards_per_pack / uncommon_fraction_denominator

    # L2
    num_packs = 10 # 10 packs of magic cards
    total_uncommon_cards = num_packs * uncommon_cards_per_pack

    # FA
    answer = total_uncommon_cards
    return answer