def solve():
    """Index: 2753.
    Returns: the total number of eyes among Nina’s pet insects.
    """
    # L1
    num_spiders = 3 # 3 spiders
    eyes_per_spider = 8 # Each spider has 8 eyes
    spider_eyes = num_spiders * eyes_per_spider

    # L2
    num_ants = 50 # 50 ants
    eyes_per_ant = 2 # Each ant has 2 eyes
    ant_eyes = num_ants * eyes_per_ant

    # L3
    total_eyes = spider_eyes + ant_eyes

    # FA
    answer = total_eyes
    return answer