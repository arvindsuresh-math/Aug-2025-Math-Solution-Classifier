def solve():
    """Index: 3791.
    Returns: the amount of money Susan had left.
    """
    # L1
    initial_money = 600 # Susan earned $600 from babysitting
    clothes_divisor = 2 # spent half of it on clothes
    spent_on_clothes = initial_money / clothes_divisor

    # L2
    money_left_after_clothes = initial_money - spent_on_clothes

    # L3
    books_divisor = 2 # spent half of what was left on books
    spent_on_books = money_left_after_clothes / books_divisor

    # L4
    final_money_left = money_left_after_clothes - spent_on_books

    # FA
    answer = final_money_left
    return answer