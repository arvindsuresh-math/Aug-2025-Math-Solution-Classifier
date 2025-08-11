def solve():
    """Index: 7261.
    Returns: the volume of fuel oil that was used between 1 November 2005 and 1 May 2006.
    """
    # L1
    initial_volume_nov_1 = 3000 # The fuel tank was then full and contained 3,000 L
    remaining_volume_jan_1 = 180 # On January 1, 2006, the tank counter indicated that 180 L remained
    consumption_nov_jan = initial_volume_nov_1 - remaining_volume_jan_1

    # L2
    volume_after_refill_jan_1 = 3000 # Mr. Fortchaud again filled his tank completely.
    remaining_volume_may_1 = 1238 # On 1 May 2006, Mr. Fortchaud decided to stop heating and he read 1,238 L on the meter.
    consumption_jan_may = volume_after_refill_jan_1 - remaining_volume_may_1

    # L3
    total_consumption = consumption_nov_jan + consumption_jan_may

    # FA
    answer = total_consumption
    return answer