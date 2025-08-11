def solve():
    """Index: 1077.
    Returns: the total number of items on the math quiz.
    """
    # L1
    total_percentage = 100 # WK
    score_percentage = 80 # Louie obtained 80% on a math quiz
    mistakes = 5 # He had 5 mistakes
    incorrect_percentage = total_percentage - score_percentage

    # L2
    items_per_percent = mistakes / incorrect_percentage

    # L3
    total_items = items_per_percent * total_percentage

    # FA
    answer = total_items
    return answer