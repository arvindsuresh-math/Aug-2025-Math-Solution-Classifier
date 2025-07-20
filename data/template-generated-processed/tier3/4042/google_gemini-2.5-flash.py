def solve():
    """Index: 4042.
    Returns: the total size of Carlson's land after buying new land.
    """
    # L1
    cost_land_1 = 8000 # land that cost $8000
    cost_per_sq_meter = 20 # costs $20 per square meter
    size_land_1 = cost_land_1 / cost_per_sq_meter

    # L2
    cost_land_2 = 4000 # additional land that cost $4000
    size_land_2 = cost_land_2 / cost_per_sq_meter

    # L3
    initial_land_size = 300 # initially owned 300 square meters of land
    total_land_size = size_land_1 + size_land_2 + initial_land_size

    # FA
    answer = total_land_size
    return answer