def solve():
    """Index: 4473.
    Returns: the total number of different books read by Tony, Dean, and Breanna.
    """
    # L1
    tony_books = 23 # Tony read 23 books
    dean_books = 12 # Dean read 12 books
    tony_dean_sum = tony_books + dean_books

    # L2
    tony_dean_duplicates = 3 # Tony and Dean read 3 of the same books
    tony_dean_unique = tony_dean_sum - tony_dean_duplicates

    # L3
    breanna_books = 17 # Breanna read 17 books
    all_three_sum = tony_dean_unique + breanna_books

    # L4
    num_readers_common_book = 3 # all three had read the same book
    desired_count = 1 # WK
    extra_count_common_to_all = num_readers_common_book - desired_count

    # L5
    total_unique_books = all_three_sum - extra_count_common_to_all

    # FA
    answer = total_unique_books
    return answer