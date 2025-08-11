def solve():
    """Index: 5261.
    Returns: the number of showers Jerry can take in July.
    """
    # L1
    pool_length = 10 # 10 feet
    pool_width = 10 # 10 feet
    pool_height = 6 # 6 feet
    pool_volume_cubic_feet = pool_length * pool_width * pool_height

    # L2
    total_allowed_gallons = 1000 # 1000 gallons of water
    drinking_cooking_gallons = 100 # 100 gallons for drinking and cooking
    gallons_remaining_for_showers = total_allowed_gallons - pool_volume_cubic_feet - drinking_cooking_gallons

    # L3
    gallons_per_shower = 20 # 20 gallons per shower
    number_of_showers = gallons_remaining_for_showers / gallons_per_shower

    # FA
    answer = number_of_showers
    return answer