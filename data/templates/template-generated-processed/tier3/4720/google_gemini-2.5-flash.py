def solve():
    """Index: 4720.
    Returns: the percentage chance of picking a blue marble.
    """
    # L1
    yellow_marbles = 20 # 20 of them are yellow
    half_divisor = 2 # half as many are green
    green_marbles = yellow_marbles / half_divisor

    # L2
    total_marbles = 60 # Cara has 60 marbles in a bag
    red_blue_marbles = total_marbles - yellow_marbles - green_marbles

    # L3
    division_half = 2 # equally divided between red and blue
    blue_marbles = red_blue_marbles / division_half

    # L4
    percentage_multiplier = 100 # multiply by 100
    blue_marble_percentage = (blue_marbles / total_marbles) * percentage_multiplier

    # FA
    answer = blue_marble_percentage
    return answer