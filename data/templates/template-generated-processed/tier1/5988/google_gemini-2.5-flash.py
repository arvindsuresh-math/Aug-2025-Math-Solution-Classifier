def solve():
    """Index: 5988.
    Returns: the total number of young fish.
    """
    # L1
    fish_per_tank = 4 # Each tank has 4 pregnant fish
    num_tanks = 3 # 3 tanks for pregnant fish
    total_pregnant_fish = fish_per_tank * num_tanks

    # L2
    young_per_fish = 20 # each fish gives birth to 20 young
    total_young_fish = total_pregnant_fish * young_per_fish

    # FA
    answer = total_young_fish
    return answer