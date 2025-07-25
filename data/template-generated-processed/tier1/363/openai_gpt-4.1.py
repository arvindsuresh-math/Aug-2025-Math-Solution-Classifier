def solve():
    """Index: 363.
    Returns: the cost of a bunch of bananas.
    """
    # L1
    tony_paid = 7 # Tony paid $7
    arnold_paid = 5 # Arnold paid $5
    tony_minus_arnold = tony_paid - arnold_paid

    # L2
    tony_apples_dozen = 2 # 2 dozen apples
    arnold_apples_dozen = 1 # 1 dozen apples
    apples_dozen_difference = tony_apples_dozen - arnold_apples_dozen

    # L3
    cost_per_dozen_apples = tony_minus_arnold # a dozen apples should cost $2

    # L4
    cost_bananas = arnold_paid - cost_per_dozen_apples

    # FA
    answer = cost_bananas
    return answer