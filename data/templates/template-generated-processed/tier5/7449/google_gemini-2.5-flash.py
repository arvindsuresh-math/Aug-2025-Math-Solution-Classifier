def solve():
    """Index: 7449.
    Returns: the number of chickens Mr. Rainwater has.
    """
    # L1
    goats_per_cow = 4 # 4 times as many goats as cows
    num_cows = 9 # 9 cows
    num_goats = goats_per_cow * num_cows

    # L2
    goats_per_chicken = 2 # 2 times as many goats as chickens
    num_chickens = num_goats / goats_per_chicken

    # FA
    answer = num_chickens
    return answer