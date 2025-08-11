def solve():
    """Index: 6827.
    Returns: the number of cranberries left.
    """
    # L1
    total_cranberries = 60000 # 60000 cranberries in a bog
    human_harvest_percent_num = 40 # 40% are harvested by humans
    percent_factor = 0.01 # WK
    human_harvested_cranberries = total_cranberries * human_harvest_percent_num * percent_factor

    # L2
    elk_eaten_cranberries = 20000 # 20000 are eaten by elk
    remaining_cranberries = total_cranberries - human_harvested_cranberries - elk_eaten_cranberries

    # FA
    answer = remaining_cranberries
    return answer