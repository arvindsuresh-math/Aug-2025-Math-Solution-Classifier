from fractions import Fraction

def solve():
    """Index: 6043.
    Returns: how many times more money he would get from melting them down instead of spending them in a store.
    """
    # L1
    quarter_weight = Fraction(1, 5) # Each quarter weighs 1/5 of an ounce
    melt_value_per_ounce = 100 # $100 per ounce
    one_ounce_for_calc = 1 # WK
    quarters_per_ounce = one_ounce_for_calc / quarter_weight

    # L2
    quarter_store_value = 0.25 # worth the regular amount
    store_value_five_quarters = quarters_per_ounce * quarter_store_value

    # L3
    melt_vs_store_ratio = melt_value_per_ounce / store_value_five_quarters

    # FA
    answer = melt_vs_store_ratio
    return answer