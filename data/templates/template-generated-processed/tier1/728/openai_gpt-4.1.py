def solve():
    """Index: 728.
    Returns: the amount of money Whitney will have left over after the purchase.
    """
    # L1
    num_posters = 2 # 2 posters
    poster_price = 5 # each poster costs $5
    poster_total = num_posters * poster_price

    # L2
    num_notebooks = 3 # 3 notebooks
    notebook_price = 4 # each notebook costs $4
    notebook_total = num_notebooks * notebook_price

    # L3
    num_bookmarks = 2 # 2 bookmarks
    bookmark_price = 2 # each bookmark costs $2
    bookmark_total = num_bookmarks * bookmark_price

    # L4
    total_purchase = poster_total + notebook_total + bookmark_total

    # L5
    num_bills = 2 # two $20 bills
    bill_value = 20 # $20 bills
    total_payment = num_bills * bill_value

    # L6
    leftover = total_payment - total_purchase

    # FA
    answer = leftover
    return answer