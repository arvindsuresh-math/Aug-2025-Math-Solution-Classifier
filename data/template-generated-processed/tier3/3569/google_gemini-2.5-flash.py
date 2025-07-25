def solve():
    """Index: 3569.
    Returns: the total number of liters in the tank.
    """
    # L1
    initial_water_volume = 6000 # A tank contains 6000 liters of water
    evaporated_volume = 2000 # 2000 liters evaporated
    volume_after_evaporation = initial_water_volume - evaporated_volume

    # L2
    drained_volume = 3500 # 3500 liters were drained by Bob
    volume_after_drain = volume_after_evaporation - drained_volume

    # L3
    rain_duration = 30 # it now rains for 30 minutes
    rain_interval = 10 # every 10 minutes
    refill_times = rain_duration / rain_interval

    # L4
    rain_amount_per_interval = 350 # 350 liters of rain are added to the tank
    total_rain_added = refill_times * rain_amount_per_interval

    # L5
    final_volume = volume_after_drain + total_rain_added

    # FA
    answer = final_volume
    return answer