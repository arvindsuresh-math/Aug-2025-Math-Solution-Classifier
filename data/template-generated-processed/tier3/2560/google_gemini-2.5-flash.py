def solve():
    """Index: 2560.
    Returns: the total amount Mr. Smith will pay.
    """
    # L1
    initial_balance = 150 # balance worth $150
    finance_charge_percentage = 2 # a 2% finance charge
    finance_charge_amount = initial_balance * finance_charge_percentage / 100

    # L2
    total_payment = initial_balance + finance_charge_amount

    # FA
    answer = total_payment
    return answer