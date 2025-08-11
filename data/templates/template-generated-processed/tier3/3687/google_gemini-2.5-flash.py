def solve():
    """Index: 3687.
    Returns: the percentage of muffins that have blueberries.
    """
    # L1
    blueberries_per_carton = 200 # 200 blueberries
    num_cartons = 3 # 3 cartons
    total_blueberries = blueberries_per_carton * num_cartons

    # L2
    blueberries_per_muffin = 10 # 10 blueberries per muffin
    blueberry_muffins = total_blueberries / blueberries_per_muffin

    # L3
    cinnamon_muffins = 60 # 60 cinnamon muffins
    total_muffins = blueberry_muffins + cinnamon_muffins

    # L4
    percentage_multiplier = 100 # 100%
    percentage_blueberry_muffins = (blueberry_muffins / total_muffins) * percentage_multiplier

    # FA
    answer = percentage_blueberry_muffins
    return answer