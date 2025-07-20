def solve():
    """Index: 5504.
    Returns: the amount of money Thomas has left over.
    """
    # L1
    num_books = 200 # Thomas owns 200 books
    price_per_book = 1.5 # Each book sells for $1.5
    money_from_books = num_books * price_per_book

    # L2
    num_records_bought = 75 # If he buys 75 records
    cost_per_record = 3 # A record costs $3
    money_spent_on_records = num_records_bought * cost_per_record

    # L3
    money_left_over = money_from_books - money_spent_on_records

    # FA
    answer = money_left_over
    return answer