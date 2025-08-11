def solve():
    """Index: 4354.
    Returns: the total number of marshmallows roasted by Joe and his dad.
    """
    # L1
    dad_marshmallows = 21 # Joe's dad has 21 marshmallows
    dad_roast_divisor = 3 # roasts a third of his marshmallows
    dad_roasted_marshmallows = dad_marshmallows / dad_roast_divisor

    # L2
    joe_multiplier = 4 # Joe has four times as much marshmallows as his dad
    joe_total_marshmallows = dad_marshmallows * joe_multiplier

    # L3
    joe_roast_divisor = 2 # Joe roasts half of his marshmallows
    joe_roasted_marshmallows = joe_total_marshmallows / joe_roast_divisor

    # L4
    total_roasted_marshmallows = dad_roasted_marshmallows + joe_roasted_marshmallows

    # FA
    answer = total_roasted_marshmallows
    return answer