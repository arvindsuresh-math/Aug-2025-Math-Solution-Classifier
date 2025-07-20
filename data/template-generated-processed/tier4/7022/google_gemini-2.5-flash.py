def solve():
    """Index: 7022.
    Returns: the number of 8-kilogram containers used.
    """
    # L1
    suki_bags = 6.5 # 6.5 bags of coffee beans
    suki_kg_per_bag = 22 # each weighed 22 kilograms
    suki_total_kg = suki_bags * suki_kg_per_bag

    # L2
    jimmy_bags = 4.5 # 4.5 bags of coffee beans
    jimmy_kg_per_bag = 18 # each weighed 18 kilograms
    jimmy_total_kg = jimmy_bags * jimmy_kg_per_bag

    # L3
    combined_kg = suki_total_kg + jimmy_total_kg

    # L4
    container_size_kg = 8 # 8-kilogram containers
    num_containers = combined_kg / container_size_kg

    # FA
    answer = num_containers
    return answer