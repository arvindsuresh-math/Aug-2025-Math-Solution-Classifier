def solve():
    """Index: 1193.
    Returns: the total amount Joe spends at the market.
    """
    # L1
    orange_price = 4.50 # fruit costs $4.50 each
    num_oranges = 3 # Joe buys 3 oranges
    orange_total = orange_price * num_oranges

    # L2
    juice_price = 0.5 # juice was 50 cents each
    num_juices = 7 # Joe buys 7 juices
    juice_total = num_juices * juice_price

    # L3
    honey_price = 5 # jars of honey were $5
    num_honey = 3 # Joe buys 3 jars of honey
    honey_total = num_honey * honey_price

    # L4
    plant_pair_price = 18 # plants were 2 for $18
    plants_per_pair = 2 # WK
    plant_unit_price = plant_pair_price / plants_per_pair

    # L5
    num_plants = 4 # Joe buys 4 plants
    plant_total = plant_unit_price * num_plants

    # L6
    total_spent = orange_total + juice_total + honey_total + plant_total

    # FA
    answer = total_spent
    return answer