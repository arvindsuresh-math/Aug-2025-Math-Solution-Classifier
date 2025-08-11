def solve():
    """Index: 5447.
    Returns: the total time it takes Jason to cook dinner.
    """
    # L1
    final_temperature = 212 # 212 degrees
    initial_temperature = 41 # 41 degree water
    temperature_increase_needed = final_temperature - initial_temperature

    # L2
    temperature_increase_per_minute = 3 # increases by 3 degrees
    time_to_boil = temperature_increase_needed / temperature_increase_per_minute

    # L3
    pasta_cook_time = 12 # cook his pasta for 12 minutes
    mixing_salad_divisor = 3 # 1/3 that long
    time_to_mix_salad = pasta_cook_time / mixing_salad_divisor

    # L4
    total_dinner_time = time_to_boil + time_to_mix_salad + pasta_cook_time

    # FA
    answer = total_dinner_time
    return answer