def solve():
    """Index: 2600.
    Returns: the additional amount of money Emir needs to buy all three books.
    """
    # L1
    cost_dictionary = 5 # dictionary that costs $5
    cost_dinosaur_book = 11 # dinosaur book that costs $11
    cost_cookbook = 5 # children's cookbook that costs $5
    total_cost = cost_dictionary + cost_dinosaur_book + cost_cookbook

    # L2
    emir_saved = 19 # saved $19 from his allowance
    money_needed = total_cost - emir_saved

    # FA
    answer = money_needed
    return answer