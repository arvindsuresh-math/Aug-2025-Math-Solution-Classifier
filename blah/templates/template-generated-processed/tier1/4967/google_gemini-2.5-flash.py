def solve():
    """Index: 4967.
    Returns: the amount of water missing for the tank to be at maximum capacity again.
    """
    # L1
    loss_rate_1 = 32000 # losing 32,000 gallons/hour
    duration_1 = 5 # for 5 hours
    loss_1 = loss_rate_1 * duration_1

    # L2
    loss_rate_2 = 10000 # losing 10,000 gallons/hour
    duration_2 = 10 # for 10 hours
    loss_2 = loss_rate_2 * duration_2

    # L3
    total_loss = loss_2 + loss_1

    # L4
    max_capacity = 350000 # maximum capacity of 350,000 gallons of water
    remaining_water_after_loss = max_capacity - total_loss

    # L5
    fill_rate = 40000 # filling it with 40,000 gallons/hour
    fill_duration = 3 # After 3 hours
    gained_water = fill_rate * fill_duration

    # L6
    current_water_after_fill = gained_water + remaining_water_after_loss

    # L7
    missing_water = max_capacity - current_water_after_fill

    # FA
    answer = missing_water
    return answer