def solve():
    """Index: 7185.
    Returns: the number of egg cartons Avery can fill.
    """
    # L1
    num_chickens = 20 # 20 chickens
    eggs_per_chicken = 6 # lays 6 eggs
    total_eggs = num_chickens * eggs_per_chicken

    # L2
    eggs_per_carton = 12 # can hold a dozen (12 eggs)
    num_cartons = total_eggs / eggs_per_carton

    # FA
    answer = num_cartons
    return answer