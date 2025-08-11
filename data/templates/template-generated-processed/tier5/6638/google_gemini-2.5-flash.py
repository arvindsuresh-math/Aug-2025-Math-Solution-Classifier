def solve():
    """Index: 6638.
    Returns: the number of zoology books Milton has.
    """
    # L3
    total_books = 80 # 80 books total
    botany_multiplier = 4 # 4 times as many books about botany
    zoology_coefficient = 1 # WK
    combined_coefficient = zoology_coefficient + botany_multiplier

    # L4
    zoology_books = total_books / combined_coefficient

    # FA
    answer = zoology_books
    return answer