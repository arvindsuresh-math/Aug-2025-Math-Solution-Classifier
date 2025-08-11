def solve():
    """Index: 3772.
    Returns: the running time of Beast of War: Armoured Command in minutes.
    """
    # L1
    hours_millennium = 2 # Millennium runs for 2 hours
    minutes_per_hour = 60 # WK
    millennium_runtime_minutes = minutes_per_hour * hours_millennium

    # L2
    alpha_epsilon_shorter_than_millennium = 30 # 30 minutes shorter than that of Millennium
    alpha_epsilon_runtime_minutes = millennium_runtime_minutes - alpha_epsilon_shorter_than_millennium

    # L3
    beast_of_war_longer_than_alpha_epsilon = 10 # 10 minutes longer than that of Alpha Epsilon
    beast_of_war_runtime_minutes = alpha_epsilon_runtime_minutes + beast_of_war_longer_than_alpha_epsilon

    # FA
    answer = beast_of_war_runtime_minutes
    return answer