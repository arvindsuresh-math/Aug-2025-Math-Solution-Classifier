def solve():
    # Books from the top section
    history_books = 12
    romance_books = 8
    poetry_books = 4

    # Books from the bottom section
    western_novels = 5
    biographies = 6

    # Half the books on the bottom section were mystery books.
    # The remaining books (Western + Biographies) constitute the other half.
    # So, the number of mystery books is equal to the sum of Western and biographies.
    mystery_books = western_novels + biographies

    # Calculate the total number of books
    total_books = history_books + romance_books + poetry_books + mystery_books + western_novels + biographies

    return total_books

# Execute the function to get the answer
answer = solve()