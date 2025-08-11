def solve():
    """Index: 4346.
    Returns: how many more liters of soda Julio has than Mateo.
    """
    # L1
    julio_orange_bottles = 4 # four bottles of orange soda
    liters_per_bottle = 2 # amount of beverage in each bottle is 2 liters
    julio_orange_liters = julio_orange_bottles * liters_per_bottle

    # L2
    julio_grape_bottles = 7 # seven bottles of grape soda
    julio_grape_liters = julio_grape_bottles * liters_per_bottle

    # L3
    julio_total_liters = julio_orange_liters + julio_grape_liters

    # L4
    mateo_orange_bottles = 1 # a bottle of orange soda
    mateo_orange_liters = mateo_orange_bottles * liters_per_bottle

    # L5
    mateo_grape_bottles = 3 # 3 bottles of grape soda
    mateo_grape_liters = mateo_grape_bottles * liters_per_bottle

    # L6
    mateo_total_liters = mateo_orange_liters + mateo_grape_liters

    # L7
    difference_in_liters = julio_total_liters - mateo_total_liters

    # FA
    answer = difference_in_liters
    return answer