from fractions import Fraction

def solve():
    """Index: 5589.
    Returns: the total number of desserts Sarah ends up with.
    """
    # L1
    total_cupcakes = 9 # her 9 cupcakes
    fraction_left_sarah = Fraction(2, 3) # WK
    cupcakes_left_sarah = fraction_left_sarah * total_cupcakes

    # L2
    cookies_from_michael = 5 # Michael saved 5 of his cookies
    total_desserts_sarah = cookies_from_michael + cupcakes_left_sarah

    # FA
    answer = total_desserts_sarah
    return answer