def solve():
    """Index: 4867.
    Returns: the amount saved in cents per apple.
    """
    # L1
    first_store_cost_dollars = 3 # $3 for 6 apples
    first_store_apples = 6 # 6 apples
    first_store_cost_per_apple_dollars = first_store_cost_dollars / first_store_apples

    # L2
    second_store_cost_dollars = 4 # $4 for 10 apples
    second_store_apples = 10 # 10 apples
    second_store_cost_per_apple_dollars = second_store_cost_dollars / second_store_apples

    # L3
    savings_per_apple_dollars = first_store_cost_per_apple_dollars - second_store_cost_per_apple_dollars

    # L4
    cents_per_dollar = 100 # WK
    savings_per_apple_cents = savings_per_apple_dollars * cents_per_dollar

    # FA
    answer = savings_per_apple_cents
    return answer