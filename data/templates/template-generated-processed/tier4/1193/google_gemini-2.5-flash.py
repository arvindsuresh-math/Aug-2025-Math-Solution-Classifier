def solve():
    """Index: 1193.
    Returns: the total amount Joe spends at the market.
    """
    # L1
    orange_cost_per_fruit = 4.50 # The fruit costs $4.50 each
    num_oranges = 3 # 3 oranges
    cost_oranges = orange_cost_per_fruit * num_oranges

    # L2
    num_juices = 7 # 7 juices
    juice_cost_per_item = 0.5 # the juice was 50 cents each
    cost_juice = num_juices * juice_cost_per_item

    # L3
    num_honey_jars = 3 # 3 jars of honey
    honey_cost_per_jar = 5 # the jars of honey were $5
    cost_honey = num_honey_jars * honey_cost_per_jar

    # L4
    plant_bundle_cost = 18 # plants were 2 for $18
    plants_per_bundle = 2 # plants were 2 for $18
    cost_per_plant = plant_bundle_cost / plants_per_bundle

    # L5
    num_plants = 4 # 4 plants
    cost_plants = cost_per_plant * num_plants

    # L6
    total_spend = cost_oranges + cost_juice + cost_honey + cost_plants

    # FA
    answer = total_spend
    return answer