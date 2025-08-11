def solve():
    """Index: 2396.
    Returns: the number of 10 oz servings of punch Carrie has.
    """
    # L1
    num_cans_mountain_dew = 6 # 6 12-oz cans of Mountain Dew
    oz_per_can_mountain_dew = 12 # 12-oz cans of Mountain Dew
    total_mountain_dew_volume = num_cans_mountain_dew * oz_per_can_mountain_dew

    # L2
    ice_volume = 28 # 28 oz of ice
    fruit_juice_volume = 40 # a 40 oz bottle of fruit juice
    total_punch_volume = total_mountain_dew_volume + ice_volume + fruit_juice_volume

    # L3
    serving_size = 10 # 10 oz servings
    num_servings = total_punch_volume / serving_size

    # FA
    answer = num_servings
    return answer