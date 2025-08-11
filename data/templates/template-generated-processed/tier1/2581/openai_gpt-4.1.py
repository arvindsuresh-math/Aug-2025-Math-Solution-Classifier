def solve():
    """Index: 2581.
    Returns: the amount of money Kenneth has left after shopping.
    """
    # L1
    num_baguettes = 2 # 2 baguettes
    cost_per_baguette = 2 # Each baguette cost $2
    cost_baguettes = num_baguettes * cost_per_baguette

    # L2
    num_bottles = 2 # 2 bottles of water
    cost_per_bottle = 1 # Each bottle of water cost $1
    cost_water = num_bottles * cost_per_bottle

    # L3
    total_cost = cost_baguettes + cost_water

    # L4
    initial_money = 50 # Kenneth has $50
    money_left = initial_money - total_cost

    # FA
    answer = money_left
    return answer