def solve():
    """Index: 2577.
    Returns: the total amount John paid for umbrellas.
    """
    # L1
    umbrellas_house = 2 # 2 umbrellas in his house
    umbrellas_car = 1 # 1 in the car
    total_umbrellas = umbrellas_house + umbrellas_car

    # L2
    cost_per_umbrella = 8 # cost $8 each
    total_cost = total_umbrellas * cost_per_umbrella

    # FA
    answer = total_cost
    return answer