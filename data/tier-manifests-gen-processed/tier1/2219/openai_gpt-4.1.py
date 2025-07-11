def solve():
    """Index: 2219.
    Returns: the number of hectares Job uses for crop production.
    """
    # L1
    house_land = 25 # 25 hectares are occupied by his house and farm machinery
    reserved_land = 15 # 15 hectares have been reserved for future expansion
    cattle_land = 40 # 40 hectares are dedicated to rearing cattle
    non_crop_land = house_land + reserved_land + cattle_land

    # L2
    total_land = 150 # he has 150 hectares of land
    crop_land = total_land - non_crop_land

    # FA
    answer = crop_land
    return answer