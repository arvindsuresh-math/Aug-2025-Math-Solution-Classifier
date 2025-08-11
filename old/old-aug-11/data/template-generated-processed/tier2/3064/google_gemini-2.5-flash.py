def solve():
    """Index: 3064.
    Returns: the total cost Jon must pay for the toaster.
    """
    # L1
    toaster_msrp = 30 # toaster that costs $30 at MSRP
    insurance_rate_decimal = 0.2 # 20% of the MSRP
    insurance_cost = toaster_msrp * insurance_rate_decimal

    # L2
    pre_tax_total = toaster_msrp + insurance_cost

    # L3
    state_tax_rate_decimal = 0.5 # state tax rate of 50%
    state_tax_amount = pre_tax_total * state_tax_rate_decimal

    # L4
    total_cost = state_tax_amount + pre_tax_total

    # FA
    answer = total_cost
    return answer