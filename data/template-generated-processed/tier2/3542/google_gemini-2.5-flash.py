def solve():
    """Index: 3542.
    Returns: the total amount of money Celine paid at the library.
    """
    # L1
    daily_charge_fifty_cents = 0.50 # fifty cents per day
    days_book1_borrowed = 20 # returned one book 20 days after borrowing it
    cost_book1 = daily_charge_fifty_cents * days_book1_borrowed

    # L2
    days_in_may = 31 # WK
    daily_charge_half_dollar = 0.5 # WK
    cost_per_book_may = days_in_may * daily_charge_half_dollar

    # L3
    num_books_remaining = 2 # the other two stayed at her house
    total_cost_books_may = cost_per_book_may * num_books_remaining

    # L4
    total_books_borrowed = 3 # borrowed three books
    total_amount_paid = total_cost_books_may + cost_book1

    # FA
    answer = total_amount_paid
    return answer