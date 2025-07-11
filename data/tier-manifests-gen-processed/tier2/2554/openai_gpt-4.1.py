def solve():
    """Index: 2554.
    Returns: the total amount Donny has to pay for all the apples.
    """
    # L1
    small_apple_price = 1.5 # Each small apple cost $1.5
    num_small_apples = 6 # Donny bought 6 small apples
    small_apples_total = small_apple_price * num_small_apples

    # L2
    medium_apple_price = 2 # medium apple cost $2
    num_medium_apples = 6 # Donny bought 6 medium apples
    medium_apples_total = medium_apple_price * num_medium_apples

    # L3
    num_big_apples = 8 # Donny bought 8 big apples
    big_apple_price = 3 # big apples cost $3
    big_apples_total = num_big_apples * big_apple_price

    # L4
    total_cost = small_apples_total + medium_apples_total + big_apples_total

    # FA
    answer = total_cost
    return answer