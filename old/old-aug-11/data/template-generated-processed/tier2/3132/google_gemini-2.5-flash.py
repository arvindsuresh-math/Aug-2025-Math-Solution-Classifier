def solve():
    """Index: 3132.
    Returns: the difference in snow accumulation between Billy Mountain/Mount Pilot and Bald Mountain in centimeters.
    """
    # L1
    bald_mountain_snow_m = 1.5 # Bald Mountain received 1.5 meters of snow
    cm_per_meter = 100 # WK
    bald_mountain_snow_cm = bald_mountain_snow_m * cm_per_meter

    # L2
    billy_mountain_snow_m = 3.5 # Billy Mountain received 3.5 meters of snow
    billy_mountain_snow_cm = billy_mountain_snow_m * cm_per_meter

    # L3
    mount_pilot_snow_cm_q = 126 # Mount Pilot received 126 centimeters of snow
    mount_pilot_snow_cm = mount_pilot_snow_cm_q

    # L4
    billy_pilot_total_cm = billy_mountain_snow_cm + mount_pilot_snow_cm

    # L5
    difference_cm = billy_pilot_total_cm - bald_mountain_snow_cm

    # FA
    answer = difference_cm
    return answer