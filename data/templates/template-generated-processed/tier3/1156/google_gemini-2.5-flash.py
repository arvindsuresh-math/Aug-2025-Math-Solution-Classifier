def solve():
    """Index: 1156.
    Returns: the profit made on Wednesday.
    """
    # L1
    total_profit = 1200 # total profit of $1,200
    monday_denominator = 3 # a third of its profit on Monday
    profit_monday = total_profit / monday_denominator

    # L2
    tuesday_denominator = 4 # a quarter of its profit on Tuesday
    profit_tuesday = total_profit / tuesday_denominator

    # L3
    profit_wednesday = total_profit - profit_monday - profit_tuesday

    # FA
    answer = profit_wednesday
    return answer