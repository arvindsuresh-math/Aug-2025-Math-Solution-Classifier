def solve():
    """Index: 2756.
    Returns: the total number of stores Super Soup had at the end of 2020.
    """
    # L1
    new_stores_2019 = 5 # opened 5 new stores
    new_stores_2020 = 10 # opened 10 new stores
    total_new_stores = new_stores_2019 + new_stores_2020

    # L2
    closed_stores_2019 = 2 # closed the 2 that performed the worst
    closed_stores_2020 = 6 # closing the 6 worst-performing
    total_closed_stores = closed_stores_2019 + closed_stores_2020

    # L3
    initial_stores_2018 = 23 # 23 stores in 2018
    final_stores = initial_stores_2018 + total_new_stores - total_closed_stores

    # FA
    answer = final_stores
    return answer