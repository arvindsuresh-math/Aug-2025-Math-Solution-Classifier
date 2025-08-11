def solve():
    """Index: 4567.
    Returns: the current number of books in the store.
    """
    # L1
    books_sold_in_store_saturday = 37 # sold 37 books in-store on Saturday
    multiplier_sunday_in_store = 2 # twice as many books in-store
    books_sold_in_store_sunday = multiplier_sunday_in_store * books_sold_in_store_saturday

    # L2
    books_sold_online_saturday = 128 # sold 128 books online
    increase_online_sunday = 34 # increased their online sales by 34 books
    books_sold_online_sunday = books_sold_online_saturday + increase_online_sunday

    # L3
    total_books_sold_weekend = books_sold_in_store_saturday + books_sold_online_saturday + books_sold_in_store_sunday + books_sold_online_sunday

    # L4
    initial_books = 743 # currently have 743 books
    books_after_sales = initial_books - total_books_sold_weekend

    # L5
    shipment_books = 160 # received a shipment of 160 books
    final_books = books_after_sales + shipment_books

    # FA
    answer = final_books
    return answer