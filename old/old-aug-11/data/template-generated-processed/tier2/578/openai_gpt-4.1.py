def solve():
    """Index: 578.
    Returns: how much more Bucky needs to save before he can buy the game.
    """
    # L1
    game_cost = 60 # costs $60
    last_weekend_earnings = 35 # earned $35 last weekend
    initial_shortfall = game_cost - last_weekend_earnings

    # L2
    total_fish_caught = 5 # caught five fish
    trout_percent = 0.6 # 60% were trout
    trout_caught = total_fish_caught * trout_percent

    # L3
    bluegill_caught = total_fish_caught - trout_caught

    # L4
    trout_earning_per_fish = 5 # $5 from trout
    trout_earnings = trout_caught * trout_earning_per_fish

    # L5
    bluegill_earning_per_fish = 4 # $4 from blue-gill
    bluegill_earnings = bluegill_caught * bluegill_earning_per_fish

    # L6
    total_earnings = trout_earnings + bluegill_earnings

    # L7
    final_shortfall = initial_shortfall - total_earnings

    # FA
    answer = final_shortfall
    return answer