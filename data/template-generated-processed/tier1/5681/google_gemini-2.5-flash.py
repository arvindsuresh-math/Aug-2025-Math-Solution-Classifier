def solve():
    """Index: 5681.
    Returns: the difference in the number of red and yellow bouncy balls Jill bought.
    """
    # L1
    red_packs = 5 # 5 packs of red bouncy balls
    balls_per_pack = 18 # Each package contained 18 bouncy balls
    red_balls = red_packs * balls_per_pack

    # L2
    yellow_packs = 4 # 4 packs of yellow bouncy balls
    yellow_balls = yellow_packs * balls_per_pack

    # L3
    difference_red_yellow = red_balls - yellow_balls

    # FA
    answer = difference_red_yellow
    return answer