def solve():
    """Index: 489.
    Returns: the difference in the bookstore's earnings on 'TOP' and 'ABC' books last week.
    """
    # L1
    num_top_sold = 13 # Thirteen "TOP" books ... were sold last week
    price_top = 8 # "TOP," costs $8
    earnings_top = num_top_sold * price_top

    # L2
    num_abc_sold = 4 # four "ABC" books were sold last week
    price_abc = 23 # "ABC," costs $23
    earnings_abc = num_abc_sold * price_abc

    # L3
    difference = earnings_top - earnings_abc

    # FA
    answer = difference
    return answer