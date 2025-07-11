def solve():
    """Index: 1576.
    Returns: the combined total number of footprints left by Pogo and Grimzi.
    """
    # L1
    pogo_footprints_per_meter = 4 # Pogo leaves 4 prints per meter
    pogo_distance = 6000 # Pogo travels 6000 meters
    pogo_total_footprints = pogo_footprints_per_meter * pogo_distance

    # L2
    grimzi_footprints_per_6m = 3 # Grimzi leaves 3 prints per 6 meters
    grimzi_distance_per_footprint = 6 # 6 meters per 3 prints
    grimzi_footprints_per_meter = grimzi_footprints_per_6m / grimzi_distance_per_footprint

    # L3
    grimzi_distance = 6000 # Grimzi travels 6000 meters
    grimzi_total_footprints = grimzi_footprints_per_meter * grimzi_distance

    # L4
    total_footprints = pogo_total_footprints + grimzi_total_footprints

    # FA
    answer = total_footprints
    return answer