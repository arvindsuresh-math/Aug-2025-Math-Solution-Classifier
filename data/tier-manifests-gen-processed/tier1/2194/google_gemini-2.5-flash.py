def solve():
    """Index: 2194.
    Returns: the number of cirrus clouds in the sky.
    """
    # L1
    cumulonimbus_clouds = 3 # 3 cumulonimbus clouds
    multiplier_cumulus_from_cumulonimbus = 12 # 12 times as many cumulus clouds as cumulonimbus clouds
    cumulus_clouds = cumulonimbus_clouds * multiplier_cumulus_from_cumulonimbus

    # L2
    multiplier_cirrus_from_cumulus = 4 # 4 times as many cirrus clouds as cumulus clouds
    cirrus_clouds = multiplier_cirrus_from_cumulus * cumulus_clouds

    # FA
    answer = cirrus_clouds
    return answer