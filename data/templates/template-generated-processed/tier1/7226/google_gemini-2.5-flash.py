def solve():
    """Index: 7226.
    Returns: the combined cost of the wallet and the purse.
    """
    # L1
    wallet_cost = 22 # wallet that costs $22
    multiplier_four_times = 4 # four times the cost of the wallet
    quadrupled_wallet_cost = wallet_cost * multiplier_four_times

    # L2
    purse_deduction = 3 # $3 less than four times the cost of the wallet
    purse_cost = quadrupled_wallet_cost - purse_deduction

    # L3
    combined_cost = purse_cost + wallet_cost

    # FA
    answer = combined_cost
    return answer