def solve():
    """Index: 2885.
    Returns: the amount of money Tina has left after her savings and spending.
    """
    # L1
    saved_june = 27 # saved $27 in June
    saved_july = 14 # saved $14 in July
    saved_august = 21 # saved $21 in August
    total_saved = saved_june + saved_july + saved_august

    # L2
    spent_books = 5 # spent $5 on books
    spent_shoes = 17 # spent $17 on new shoes
    total_spent = spent_books + spent_shoes

    # L3
    money_left = total_saved - total_spent

    # FA
    answer = money_left
    return answer