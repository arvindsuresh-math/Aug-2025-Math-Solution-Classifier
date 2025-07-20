def solve():
    """Index: 6111.
    Returns: the total amount Tara spends on gas for her road trip.
    """
    # L1
    tank_capacity = 12 # 12-gallon tank
    price_station1 = 3 # $3
    cost_station1 = tank_capacity * price_station1

    # L2
    price_station2 = 3.5 # $3.50
    cost_station2 = tank_capacity * price_station2

    # L3
    price_station3 = 4 # $4
    cost_station3 = tank_capacity * price_station3

    # L4
    price_station4 = 4.5 # $4.50
    cost_station4 = tank_capacity * price_station4

    # L5
    total_gas_cost = cost_station1 + cost_station2 + cost_station3 + cost_station4

    # FA
    answer = total_gas_cost
    return answer