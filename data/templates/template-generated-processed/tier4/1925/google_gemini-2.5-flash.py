def solve():
    """Index: 1925.
    Returns: the total time Tyson spent in his races.
    """
    # L1
    total_races = 10 # ten total races
    races_half_divisor = 2 # half his races happened in lakes and half his races happened in the ocean
    num_lake_races = total_races / races_half_divisor

    # L2
    num_ocean_races = total_races / races_half_divisor

    # L3
    race_distance_miles = 3 # each of which was 3 miles long
    total_lake_miles = num_lake_races * race_distance_miles

    # L4
    speed_used_for_lake_calculation = 2.5 # 2.5 mph in an ocean
    time_lake_races_hours = total_lake_miles / speed_used_for_lake_calculation

    # L5
    total_ocean_miles = num_ocean_races * race_distance_miles

    # L6
    speed_used_for_ocean_calculation = 3 # 3 miles per hour in a lake
    time_ocean_races_hours = total_ocean_miles / speed_used_for_ocean_calculation

    # L7
    total_time_racing_hours = time_ocean_races_hours + time_lake_races_hours

    # FA
    answer = total_time_racing_hours
    return answer