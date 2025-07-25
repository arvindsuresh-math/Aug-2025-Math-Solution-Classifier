def solve():
    """Index: 2756.
    Returns: the number of Super Soup stores at the end of 2020.
    """
    # L1
    stores_opened_2019 = 5 # opened 5 new stores in 2019
    stores_opened_2020 = 10 # opened 10 new stores in 2020
    total_opened = stores_opened_2019 + stores_opened_2020

    # L2
    stores_closed_2019 = 2 # closed the 2 that performed the worst in 2019
    stores_closed_2020 = 6 # closing the 6 worst-performing in 2020
    total_closed = stores_closed_2019 + stores_closed_2020

    # L3
    initial_stores = 23 # had 23 stores in 2018
    final_stores = initial_stores + total_opened - total_closed

    # FA
    answer = final_stores
    return answer