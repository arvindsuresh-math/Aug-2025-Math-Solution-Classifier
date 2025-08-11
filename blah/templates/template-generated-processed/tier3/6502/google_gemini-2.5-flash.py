def solve():
    """Index: 6502.
    Returns: the total amount of money Ivan has in dollars.
    """
    # L1
    num_dimes_per_bank = 50 # 50 dimes
    cents_per_dime = 10 # WK
    cents_from_dimes_per_bank = num_dimes_per_bank * cents_per_dime

    # L2
    num_pennies_per_bank = 100 # 100 pennies
    total_cents_per_bank = num_pennies_per_bank + cents_from_dimes_per_bank

    # L3
    cents_per_dollar = 100 # WK
    dollars_per_bank = total_cents_per_bank / cents_per_dollar

    # L4
    num_piggy_banks = 2 # two piggy banks
    total_dollars = dollars_per_bank * num_piggy_banks

    # FA
    answer = total_dollars
    return answer