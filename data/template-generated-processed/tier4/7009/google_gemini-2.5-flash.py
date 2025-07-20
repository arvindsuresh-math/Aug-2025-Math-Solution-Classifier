def solve():
    """Index: 7009.
    Returns: the number of books Pablo read.
    """
    # L1
    cent_per_page = 0.01 # one cent for every page
    pages_per_book = 150 # exactly 150 pages
    dollars_per_book = cent_per_page * pages_per_book

    # L2
    candy_cost = 15 # $15 worth of candy
    money_leftover = 3 # $3 leftover
    total_earned_dollars = candy_cost + money_leftover

    # L3
    num_books_read = total_earned_dollars / dollars_per_book

    # FA
    answer = num_books_read
    return answer