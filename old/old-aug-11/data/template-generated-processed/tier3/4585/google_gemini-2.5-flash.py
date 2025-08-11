def solve():
    """Index: 4585.
    Returns: the number of portions of milk Jasmine can pour.
    """
    # L1
    ml_per_liter = 1000 # WK
    container_liters = 2 # a full 2-liter container
    total_ml = ml_per_liter * container_liters

    # L2
    portion_ml = 200 # 200 ml milk
    num_portions = total_ml / portion_ml

    # FA
    answer = num_portions
    return answer