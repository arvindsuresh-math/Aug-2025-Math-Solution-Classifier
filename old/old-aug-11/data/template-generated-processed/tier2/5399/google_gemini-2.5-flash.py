def solve():
    """Index: 5399.
    Returns: the amount of money Steve kept not counting the money from the advance.
    """
    # L1
    total_copies_sold = 1000000 # sells 1,000,000 copies
    copies_covered_by_advance = 100000 # advance to pay for 100,000 copies
    copies_sold_after_advance = total_copies_sold - copies_covered_by_advance

    # L2
    price_per_copy = 2 # $2 for each copy of the book sold
    money_from_sales = copies_sold_after_advance * price_per_copy

    # L3
    agent_commission_decimal = 0.1 # 10% of that
    agent_cut = money_from_sales * agent_commission_decimal

    # L4
    money_kept = money_from_sales - agent_cut

    # FA
    answer = money_kept
    return answer