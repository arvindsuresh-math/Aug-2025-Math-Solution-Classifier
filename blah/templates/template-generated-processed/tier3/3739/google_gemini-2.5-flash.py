def solve():
    """Index: 3739.
    Returns: the total number of marshmallows held by all three kids.
    """
    # L1
    haley_marshmallows = 8 # Haley could hold 8 marshmallows

    # L2
    michael_multiplier = 3 # 3 times as many marshmallows as Haley
    michael_marshmallows = haley_marshmallows * michael_multiplier

    # L3
    brandon_divisor = 2 # half as many as Michael
    brandon_marshmallows = michael_marshmallows / brandon_divisor

    # L4
    total_marshmallows = haley_marshmallows + michael_marshmallows + brandon_marshmallows

    # FA
    answer = total_marshmallows
    return answer