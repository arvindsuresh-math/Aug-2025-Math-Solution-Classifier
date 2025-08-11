def solve():
    """Index: 2845.
    Returns: the number of mosquitoes that would have to feed to kill someone.
    """
    # L1
    drops_per_feeding = 20 # 20 drops of blood every time it feeds
    drops_per_liter = 5000 # 5000 drops per liter
    liters_per_feeding = drops_per_feeding / drops_per_liter

    # L2
    lethal_blood_liters = 3 # 3 liters of blood to die
    num_mosquitoes = lethal_blood_liters / liters_per_feeding

    # FA
    answer = num_mosquitoes
    return answer