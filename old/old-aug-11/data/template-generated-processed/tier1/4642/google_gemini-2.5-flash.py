def solve():
    """Index: 4642.
    Returns: the number of books they still have to read.
    """
    # L1
    mcgregor_finished = 34 # Mcgregor was able to finish 34
    floyd_finished = 32 # Floyd was able to finish 32
    total_finished = mcgregor_finished + floyd_finished

    # L2
    total_assigned_books = 89 # assigned 89 books to read
    books_remaining = total_assigned_books - total_finished

    # FA
    answer = books_remaining
    return answer