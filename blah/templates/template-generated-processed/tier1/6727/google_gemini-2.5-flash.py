def solve():
    """Index: 6727.
    Returns: the total number of animals Cara's cat catches.
    """
    # L1
    rats_martha = 3 # 3 rats
    birds_martha = 7 # 7 birds
    total_martha_animals = rats_martha + birds_martha

    # L2
    multiplier_cara = 5 # five times as many animals
    five_times_martha = total_martha_animals * multiplier_cara

    # L3
    less_cara = 3 # 3 less than five times as many animals
    total_cara_animals = five_times_martha - less_cara

    # FA
    answer = total_cara_animals
    return answer