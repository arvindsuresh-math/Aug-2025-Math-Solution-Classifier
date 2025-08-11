def solve():
    """Index: 1209.
    Returns: the number of gold bars Jame has left after taxes and divorce.
    """
    # L1
    initial_bars = 60 # Jame has 60 bars of gold
    tax_fraction = 0.1 # uses 10% of them to pay for tax
    bars_lost_to_taxes = initial_bars * tax_fraction

    # L2
    bars_after_taxes = initial_bars - bars_lost_to_taxes

    # L3
    divorce_divisor = 2 # loses half of what is left in divorce
    bars_after_divorce = bars_after_taxes / divorce_divisor

    # FA
    answer = bars_after_divorce
    return answer