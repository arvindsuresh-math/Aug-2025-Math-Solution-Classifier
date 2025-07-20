def solve():
    """Index: 5522.
    Returns: the number of sweet potatoes not yet sold.
    """
    # L1
    sold_to_mrs_adams = 20 # sold 20 of them to Mrs. Adams
    sold_to_mr_lenon = 15 # and 15 of them to Mr. Lenon
    total_sold = sold_to_mrs_adams + sold_to_mr_lenon

    # L2
    total_harvested = 80 # harvested 80 sweet potatoes
    not_yet_sold = total_harvested - total_sold

    # FA
    answer = not_yet_sold
    return answer