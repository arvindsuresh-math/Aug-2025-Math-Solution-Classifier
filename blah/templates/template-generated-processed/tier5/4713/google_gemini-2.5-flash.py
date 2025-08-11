def solve():
    """Index: 4713.
    Returns: the number of apples Sara ate.
    """
    # L5
    ali_multiplier = 4 # Ali ate 4 times more apples than Sara
    total_apples = 80 # Ali and Sara ate 80 small apples combined
    combined_coefficient = ali_multiplier + 1

    # L6
    sara_apples = total_apples / combined_coefficient

    # FA
    answer = sara_apples
    return answer