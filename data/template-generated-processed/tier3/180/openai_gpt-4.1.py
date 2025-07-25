def solve():
    """Index: 180.
    Returns: the amount of money Derek has left after buying textbooks and school supplies.
    """
    # L1
    initial_money = 960 # Derek has $960 to buy his books for the semester
    textbook_divisor = 2 # spends half of that on his textbooks
    spent_on_textbooks = initial_money / textbook_divisor

    # L2
    supplies_divisor = 4 # spends a quarter of what is left on his school supplies
    spent_on_supplies = spent_on_textbooks / supplies_divisor

    # L3
    amount_left = initial_money - spent_on_textbooks - spent_on_supplies

    # FA
    answer = amount_left
    return answer