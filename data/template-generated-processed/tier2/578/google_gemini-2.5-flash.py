def solve():
    """Index: 578.
    Returns: how much more Bucky needs to save before he can buy the game.
    """
    # L1
    game_cost = 60 # costs $60
    earned_last_weekend = 35 # earned $35
    initial_shortfall = game_cost - earned_last_weekend

    # L2
    total_fish_caught = 5 # caught five fish this Sunday
    trout_percentage_decimal = 0.6 # 60% were trout
    num_trout = total_fish_caught * trout_percentage_decimal

    # L3
    num_bluegill = total_fish_caught - num_trout

    # L4
    trout_value = 5 # earn $5 from trout
    earned_from_trout = num_trout * trout_value

    # L5
    bluegill_value = 4 # $4 from blue-gill
    earned_from_bluegill = num_bluegill * bluegill_value

    # L6
    earned_this_sunday = earned_from_trout + earned_from_bluegill

    # L7
    remaining_shortfall = initial_shortfall - earned_this_sunday

    # FA
    answer = remaining_shortfall
    return answer