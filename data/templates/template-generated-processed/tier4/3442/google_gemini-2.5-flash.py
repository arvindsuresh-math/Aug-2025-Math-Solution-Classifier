from fractions import Fraction

def solve():
    """Index: 3442.
    Returns: the total amount Gary will earn.
    """
    # L1
    flour_for_cakes = 4 # 4 pounds of flour to make cakes
    flour_per_cake = 0.5 # 0.5 pounds of flour each
    num_cakes = flour_for_cakes / flour_per_cake

    # L2
    remaining_flour = 2 # remaining 2 pounds of flour
    flour_per_cupcake = Fraction(1, 5) # 1/5 pounds of flour
    num_cupcakes = remaining_flour / flour_per_cupcake

    # L3
    cake_price = 2.5 # sell the cakes for $2.5 each
    earnings_from_cakes = cake_price * num_cakes

    # Calculate earnings from cupcakes (not a distinct solution line)
    cupcake_price = 1 # cupcakes for $1 each
    earnings_from_cupcakes = cupcake_price * num_cupcakes

    # L4
    total_earnings = earnings_from_cakes + earnings_from_cupcakes

    # FA
    answer = total_earnings
    return answer