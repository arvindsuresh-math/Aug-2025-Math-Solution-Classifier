def solve():
    """Index: 6351.
    Returns: how many kilometers longer Telegraph Road is than Pardee Road.
    """
    # L1
    telegraph_road_km = 162 # 162 kilometers long
    meters_per_km = 1000 # WK
    telegraph_road_m = telegraph_road_km * meters_per_km

    # L2
    pardee_road_m = 12000 # 12000 meters long

    # L3
    difference_m = telegraph_road_m - pardee_road_m

    # L4
    difference_km = difference_m / meters_per_km

    # FA
    answer = difference_km
    return answer