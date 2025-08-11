def solve():
    """Index: 3027.
    Returns: the number of books Mary had at the end of the year.
    """
    # L1
    books_per_month_club = 1 # 1 book each month
    months_in_year = 12 # WK
    books_from_club = books_per_month_club * months_in_year

    # L2
    books_bought_bookstore = 5 # bought 5 more books
    books_bought_yardsale = 2 # bought 2 books at yard sales
    books_bought_total = books_bought_bookstore + books_bought_yardsale

    # L3
    books_given_daughter = 1 # daughter gave her another book
    books_given_mother = 4 # mother gave her a series of 4 books
    books_given_total = books_given_daughter + books_given_mother

    # L4
    books_donated = 12 # donated 12 books
    books_sold = 3 # sold 3 to a used book store
    books_got_rid_of_total = books_donated + books_sold

    # L5
    initial_books = 72 # started with 72 mystery books
    final_books = initial_books + books_from_club + books_bought_total + books_given_total - books_got_rid_of_total

    # FA
    answer = final_books
    return answer