from fractions import Fraction

def solve():
    """Index: 2153.
    Returns: the total number of times Felicia fills her measuring scoop.
    """
    # L1
    flour_cups = 2 # 2 cups of flour
    scoop_size = Fraction(1, 4) # 1/4 cup
    flour_fills = flour_cups / scoop_size

    # L2
    white_sugar_cups = 1 # a cup of white sugar
    white_sugar_fills = white_sugar_cups / scoop_size

    # L3
    oil_cups = Fraction(1, 2) # a 1/2 cup of oil
    oil_fills = oil_cups / scoop_size

    # L4
    brown_sugar_cups = Fraction(1, 4) # a 1/4 cup of brown sugar
    brown_sugar_fills = 1

    # L5
    total_fills = flour_fills + white_sugar_fills + oil_fills + brown_sugar_fills

    # FA
    answer = total_fills
    return answer