def solve():
    """Index: 240.
    Returns: the number of more red bouncy balls than yellow bouncy balls Kate bought.
    """
    # L1
    red_packs = 7 # 7 packs of red bouncy balls
    balls_per_pack = 18 # Each pack contained 18 bouncy balls
    red_bouncy_balls = red_packs * balls_per_pack

    # L2
    yellow_packs = 6 # 6 packs of yellow bouncy balls
    yellow_bouncy_balls = yellow_packs * balls_per_pack

    # L3
    difference = red_bouncy_balls - yellow_bouncy_balls

    # FA
    answer = difference
    return answer