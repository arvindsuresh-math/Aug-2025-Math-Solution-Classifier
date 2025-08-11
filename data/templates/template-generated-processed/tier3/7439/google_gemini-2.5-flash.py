def solve():
    """Index: 7439.
    Returns: the total number of oranges left uneaten.
    """
    # L1
    total_oranges = 96 # Of 96 oranges
    ripe_divisor = 2 # half were ripe
    ripe_oranges = total_oranges / ripe_divisor

    # L2
    ripe_eaten_divisor = 4 # 1/4 of the ripe oranges were eaten
    ripe_oranges_eaten = ripe_oranges / ripe_eaten_divisor

    # L3
    unripe_oranges = total_oranges - ripe_oranges
    unripe_eaten_divisor = 8 # 1/8 of the unripe oranges were eaten
    unripe_oranges_eaten = unripe_oranges / unripe_eaten_divisor

    # L4
    total_eaten_oranges = ripe_oranges_eaten + unripe_oranges_eaten

    # L5
    oranges_left_uneaten = total_oranges - total_eaten_oranges

    # FA
    answer = oranges_left_uneaten
    return answer