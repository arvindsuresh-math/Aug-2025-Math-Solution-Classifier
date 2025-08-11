def solve():
    """Index: 6601.
    Returns: the total ounces of artichoke dip Hakeem can make.
    """
    # L1
    total_money = 15 # He has $15 dollars
    cost_per_artichoke = 1.25 # artichokes cost $1.25 each
    num_artichokes_bought = total_money / cost_per_artichoke

    # L2
    ounces_per_batch = 5 # 5 ounces of dip
    artichokes_per_batch = 3 # 3 artichokes
    ounces_per_artichoke_val = ounces_per_batch / artichokes_per_batch

    # L3
    intermediate_numerator = num_artichokes_bought * ounces_per_batch
    intermediate_denominator = artichokes_per_batch
    total_ounces_dip = intermediate_numerator / intermediate_denominator

    # FA
    answer = total_ounces_dip
    return answer