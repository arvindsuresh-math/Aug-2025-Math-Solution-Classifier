def solve():
    """Index: 2194.
    Returns: the number of cirrus clouds in the sky at this moment.
    """
    # L1
    cumulonimbus_clouds = 3 # sky currently has 3 cumulonimbus clouds
    cumulus_per_cumulonimbus = 12 # 12 times as many cumulus clouds as cumulonimbus clouds
    cumulus_clouds = cumulonimbus_clouds * cumulus_per_cumulonimbus

    # L2
    cirrus_per_cumulus = 4 # 4 times as many cirrus clouds as cumulus clouds
    cirrus_clouds = cirrus_per_cumulus * cumulus_clouds

    # FA
    answer = cirrus_clouds
    return answer