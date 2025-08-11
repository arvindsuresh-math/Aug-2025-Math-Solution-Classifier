def solve():
    """Index: 1925.
    Returns: the total time Tyson spent in his races (in hours).
    """
    # L1
    total_races = 10 # ten total races
    races_per_type = total_races / 2

    # L2
    # (identical to L1, so races_per_type is reused)

    # L3
    miles_per_race = 3 # each race was 3 miles long
    lake_races_miles = races_per_type * miles_per_race

    # L4
    lake_speed = 2.5 # 2.5 mph in an ocean (but L4 is for lake, see L6 for ocean)
    lake_time = lake_races_miles / lake_speed

    # L5
    ocean_races_miles = races_per_type * miles_per_race

    # L6
    ocean_speed = 3 # 3 mph in a lake (but L6 is for ocean, see L4 for lake)
    ocean_time = ocean_races_miles / ocean_speed

    # L7
    total_time = ocean_time + lake_time

    # FA
    answer = total_time
    return answer