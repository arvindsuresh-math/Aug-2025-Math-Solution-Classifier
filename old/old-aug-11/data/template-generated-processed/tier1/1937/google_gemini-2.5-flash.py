def solve():
    """Index: 1937.
    Returns: the net increase in the number of bicycles in stock.
    """
    # L1
    sold_friday = 10 # sold 10 bicycles
    sold_saturday = 12 # sold 12 bicycles
    sold_sunday = 9 # sold 9 bicycles
    total_sold_bicycles = sold_friday + sold_saturday + sold_sunday

    # L2
    bought_friday = 15 # bought an additional 15
    bought_saturday = 8 # bought 8 more
    bought_sunday = 11 # bought 11 more
    total_bought_bicycles = bought_friday + bought_saturday + bought_sunday

    # L3
    net_increase = total_bought_bicycles - total_sold_bicycles

    # FA
    answer = net_increase
    return answer