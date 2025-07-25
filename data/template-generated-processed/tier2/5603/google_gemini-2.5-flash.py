def solve():
    """Index: 5603.
    Returns: the new speed of the car.
    """
    # L1
    original_speed = 150 # car's original speed was 150 mph
    speed_increase_percent_decimal = 0.3 # increases his car's speed by 30%
    speed_increase_amount_percent = original_speed * speed_increase_percent_decimal

    # L2
    speed_after_supercharge = original_speed + speed_increase_amount_percent

    # L3
    additional_speed_increase = 10 # increases the speed a further 10 mph
    final_speed = speed_after_supercharge + additional_speed_increase

    # FA
    answer = final_speed
    return answer