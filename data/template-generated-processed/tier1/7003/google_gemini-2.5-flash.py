def solve():
    """Index: 7003.
    Returns: the total number of balls Julia bought.
    """
    # L1
    red_packs = 3 # 3 packs of red balls
    yellow_packs = 10 # 10 packs of yellow balls
    green_packs = 8 # 8 packs of green balls
    total_packs = red_packs + yellow_packs + green_packs

    # L2
    balls_per_package = 19 # 19 balls in each package
    total_balls = total_packs * balls_per_package

    # FA
    answer = total_balls
    return answer