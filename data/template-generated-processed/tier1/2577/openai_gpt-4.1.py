def solve():
    """Index: 2577.
    Returns: the total amount John paid for all his umbrellas.
    """
    # L1
    umbrellas_house = 2 # 2 umbrellas in his house
    umbrellas_car = 1 # 1 in the car
    total_umbrellas = umbrellas_house + umbrellas_car

    # L2
    umbrella_cost = 8 # cost $8 each
    total_cost = total_umbrellas * umbrella_cost

    # FA
    answer = total_cost
    return answer