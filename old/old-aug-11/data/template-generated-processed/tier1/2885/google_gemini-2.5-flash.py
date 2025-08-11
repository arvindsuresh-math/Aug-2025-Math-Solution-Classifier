def solve():
    """Index: 2885.
    Returns: the amount of money Tina has left.
    """
    # L1
    june_saved = 27 # Tina saved $27 in June
    july_saved = 14 # $14 in July
    august_saved = 21 # and $21 in August
    total_saved = june_saved + july_saved + august_saved

    # L2
    spent_on_books = 5 # spent $5 on books
    spent_on_shoes = 17 # and $17 on new shoes
    total_spent = spent_on_books + spent_on_shoes

    # L3
    money_left = total_saved - total_spent

    # FA
    answer = money_left
    return answer