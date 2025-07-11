def solve():
    """Index: 1473.
    Returns: the number of books sold in March.
    """
    # L1
    average_books_per_month = 16 # average number of books he sold per month across all three months is 16
    num_months = 3 # across all three months
    total_books_3_months = num_months * average_books_per_month

    # L2
    january_sales = 15 # 15 books in January
    february_sales = 16 # 16 in February
    jan_feb_sales = january_sales + february_sales

    # L3
    march_sales = total_books_3_months - jan_feb_sales

    # FA
    answer = march_sales
    return answer