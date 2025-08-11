def solve():
    """Index: 5832.
    Returns: the total number of steaks Harvey sold.
    """
    # L1
    initial_steaks = 25 # started out with 25 steaks
    steaks_left_first_sale = 12 # only had 12 steaks left
    steaks_sold_first = initial_steaks - steaks_left_first_sale

    # L2
    steaks_sold_second = 4 # sold 4 more steaks
    total_steaks_sold = steaks_sold_first + steaks_sold_second

    # FA
    answer = total_steaks_sold
    return answer