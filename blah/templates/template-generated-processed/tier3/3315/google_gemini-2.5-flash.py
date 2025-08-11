def solve():
    """Index: 3315.
    Returns: the total number of doors the factory will produce.
    """
    # L1
    initial_production = 200 # planning to produce 200 cars
    shortage_reduction = 50 # decreased the production by 50 cars
    cars_after_shortage = initial_production - shortage_reduction

    # L2
    pandemic_reduction_divisor = 2 # cut production by another 50%
    cars_after_pandemic = cars_after_shortage / pandemic_reduction_divisor

    # L3
    doors_per_car = 5 # cars with 5 doors
    total_doors = cars_after_pandemic * doors_per_car

    # FA
    answer = total_doors
    return answer