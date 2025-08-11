def solve():
    """Index: 5897.
    Returns: the total number of toy cars Olaf has after receiving gifts.
    """
    # L2
    dad_cars = 10 # Dad gave Olaf 10 toy cars
    mom_more_than_dad = 5 # 5 less than Mum (Dad gave 5 less than Mum)
    mom_cars = dad_cars + mom_more_than_dad

    # L4
    auntie_cars = 6 # Auntie gave Olaf 6 toy cars
    uncle_less_than_auntie = 1 # 1 more than the uncle (Auntie gave 1 more than uncle)
    uncle_cars = auntie_cars - uncle_less_than_auntie

    # L5
    grandpa_multiplier = 2 # twice as many toy cars as the uncle
    grandpa_cars = grandpa_multiplier * uncle_cars

    # L6
    total_gifts = dad_cars + mom_cars + auntie_cars + uncle_cars + grandpa_cars

    # L7
    initial_collection = 150 # his collection consisted of 150 cars
    final_collection = initial_collection + total_gifts

    # FA
    answer = final_collection
    return answer