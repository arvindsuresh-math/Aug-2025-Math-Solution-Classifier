def solve():
    """Index: 5634.
    Returns: the total amount the author earned.
    """
    # L1
    paper_cover_price_per_copy = 0.20 # $0.20 each
    paper_cover_copies_sold = 32000 # 32,000 copies
    paper_cover_total_sales = paper_cover_price_per_copy * paper_cover_copies_sold

    # L2
    author_royalty_paper_cover_numerator = 6 # 6% of the total sales
    percentage_divisor = 100 # WK
    author_earnings_paper_cover = paper_cover_total_sales * author_royalty_paper_cover_numerator / percentage_divisor

    # L3
    hardcover_price_per_copy = 0.40 # $0.40 each
    hardcover_copies_sold = 15000 # 15,000 copies
    hardcover_total_sales = hardcover_price_per_copy * hardcover_copies_sold

    # L4
    author_royalty_hardcover_numerator = 12 # 12% of the total sales
    author_earnings_hardcover = hardcover_total_sales * author_royalty_hardcover_numerator / percentage_divisor

    # L5
    total_author_earnings = author_earnings_paper_cover + author_earnings_hardcover

    # FA
    answer = total_author_earnings
    return answer