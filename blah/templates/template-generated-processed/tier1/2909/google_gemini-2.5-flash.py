def solve():
    """Index: 2909.
    Returns: the total amount of money Alan spent at the market.
    """
    # L1
    num_eggs = 20 # bought 20 eggs
    price_per_egg = 2 # $2 per egg
    cost_eggs = num_eggs * price_per_egg

    # L2
    num_chickens = 6 # bought 6 chickens
    price_per_chicken = 8 # $8 per chicken
    cost_chickens = num_chickens * price_per_chicken

    # L3
    total_spent = cost_eggs + cost_chickens

    # FA
    answer = total_spent
    return answer