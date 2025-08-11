def solve():
    """Index: 3025.
    Returns: the total weight of the load of crates and cartons.
    """
    # L1
    num_crates = 12 # 12 crates
    weight_per_crate = 4 # 4 kilograms
    weight_crates = num_crates * weight_per_crate

    # L2
    num_cartons = 16 # 16 cartons
    weight_per_carton = 3 # 3 kilograms
    weight_cartons = num_cartons * weight_per_carton

    # L3
    total_weight = weight_crates + weight_cartons

    # FA
    answer = total_weight
    return answer