def solve():
    """Index: 4087.
    Returns: the longest boat length Mitch can buy in feet.
    """
    # L1
    license_registration_fee = 500 # keep $500 for a license and registration
    docking_fee_multiplier = 3 # three times that amount for docking fees
    docking_fees = license_registration_fee * docking_fee_multiplier

    # L2
    total_fees = license_registration_fee + docking_fee_multiplier * license_registration_fee

    # L3
    initial_savings = 20000 # saved $20000
    money_for_boat = initial_savings - total_fees

    # L4
    cost_per_foot = 1500 # $1500 per foot in length
    longest_boat_length = money_for_boat / cost_per_foot

    # FA
    answer = longest_boat_length
    return answer