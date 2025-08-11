from fractions import Fraction

def solve():
    """Index: 7132.
    Returns: the total amount Anna earned.
    """
    # L1
    num_trays = 4 # four baking trays
    cupcakes_per_tray = 20 # Each tray has 20 cupcakes
    total_cupcakes_baked = num_trays * cupcakes_per_tray

    # L2
    fraction_sold = Fraction(3, 5) # 3/5 of the cupcakes were sold
    cupcakes_sold = total_cupcakes_baked * fraction_sold

    # L3
    price_per_cupcake = 2 # each cupcake was then sold for $2
    total_earned = cupcakes_sold * price_per_cupcake

    # FA
    answer = total_earned
    return answer