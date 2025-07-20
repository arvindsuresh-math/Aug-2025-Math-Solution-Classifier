def solve():
    """Index: 4302.
    Returns: the total number of pizzas and hot dogs made in June.
    """
    # L1
    hot_dogs_per_day = 60 # 60 hot dogs every day
    more_pizzas_than_hot_dogs = 40 # 40 more pizzas than hot dogs
    pizzas_per_day = hot_dogs_per_day + more_pizzas_than_hot_dogs

    # L2
    total_per_day = pizzas_per_day + hot_dogs_per_day

    # L3
    days_in_june = 30 # WK
    total_in_june = days_in_june * total_per_day

    # FA
    answer = total_in_june
    return answer