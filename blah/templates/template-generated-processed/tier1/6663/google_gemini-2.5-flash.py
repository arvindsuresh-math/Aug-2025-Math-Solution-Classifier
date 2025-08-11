def solve():
    """Index: 6663.
    Returns: how much faster the bullet flies when fired in the same direction as the horse.
    """
    # L1
    bullet_speed_from_gun = 400 # a bullet fired from his gun flies at a speed of 400 feet per second
    horse_speed = 20 # His horse runs at 20 feet per second
    speed_same_direction = bullet_speed_from_gun + horse_speed

    # L2
    speed_opposite_direction = bullet_speed_from_gun - horse_speed

    # L3
    speed_difference = speed_same_direction - speed_opposite_direction

    # FA
    answer = speed_difference
    return answer