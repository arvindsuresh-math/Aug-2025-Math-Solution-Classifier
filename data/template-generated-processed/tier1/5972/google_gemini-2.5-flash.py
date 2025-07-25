def solve():
    """Index: 5972.
    Returns: the total soaking time for the clothes.
    """
    # L1
    grass_stain_soak_time_per_stain = 4 # 4 minutes to get rid of each grass stain
    num_grass_stains = 3 # 3 grass stains
    total_grass_stain_soak_time = grass_stain_soak_time_per_stain * num_grass_stains

    # L2
    marinara_stain_soak_time = 7 # 7 additional minutes to get rid of each marinara stain and 1 marinara stain
    total_soak_time = total_grass_stain_soak_time + marinara_stain_soak_time

    # FA
    answer = total_soak_time
    return answer