def solve():
    """Index: 1209.
    Returns: the number of gold bars Jame has left.
    """
    # L1
    initial_gold_bars = 60 # Jame has 60 bars of gold
    tax_percentage = 0.1 # uses 10% of them to pay for tax
    gold_lost_to_taxes = initial_gold_bars * tax_percentage

    # L2
    gold_after_taxes = initial_gold_bars - gold_lost_to_taxes

    # L3
    divorce_divisor = 2 # loses half of what is left in divorce
    gold_after_divorce = gold_after_taxes / divorce_divisor

    # FA
    answer = gold_after_divorce
    return answer