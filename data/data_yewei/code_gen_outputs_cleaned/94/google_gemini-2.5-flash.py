def solve_94():
    """
    Calculates the time it will take John to write a certain number of books.

    John writes 20 pages a day.
    He needs to write 3 books that are 400 pages each.
    """
    pages_per_day = 20
    num_books = 3
    pages_per_book = 400

    # Calculate the total number of pages John needs to write
    total_pages_to_write = num_books * pages_per_book

    # Calculate the number of days it will take him
    days_needed = total_pages_to_write / pages_per_day

    return int(days_needed)

# Example usage:
# print(solve_94())