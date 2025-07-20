def solve():
    """Index: 5355.
    Returns: the total number of flowers on the porch.
    """
    # L1
    total_plants = 80 # 80 plants
    flowering_plant_percentage = 0.40 # 40% of her plants are flowering plants
    num_flowering_plants = total_plants * flowering_plant_percentage

    # L2
    porch_fraction_divisor = 4 # a fourth of her flowering plants
    num_flowering_plants_on_porch = num_flowering_plants / porch_fraction_divisor

    # L3
    flowers_per_plant = 5 # each flowering plant produces 5 flowers
    total_flowers_on_porch = num_flowering_plants_on_porch * flowers_per_plant

    # FA
    answer = total_flowers_on_porch
    return answer