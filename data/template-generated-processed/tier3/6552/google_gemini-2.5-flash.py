def solve():
    """Index: 6552.
    Returns: the number of jars of strawberry jelly sold.
    """
    # L1
    raspberry_multiplier = 2 # twice as much as strawberry jelly
    plum_jelly_sold = 6 # sold 6 jars of plum jelly today
    raspberry_jelly_sold = raspberry_multiplier * plum_jelly_sold

    # L2
    grape_multiplier = 3 # a third as much as the grape jelly
    grape_jelly_sold = raspberry_jelly_sold * grape_multiplier

    # L3
    strawberry_divisor = 2 # twice as much as the strawberry jelly
    strawberry_jelly_sold = grape_jelly_sold / strawberry_divisor

    # FA
    answer = strawberry_jelly_sold
    return answer