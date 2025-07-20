def solve():
    """Index: 4966.
    Returns: Paul's account balance after the transfers and reversal.
    """
    # L1
    service_charge_percent_numerator = 2 # 2% was added to each transaction
    percent_denominator = 100 # WK
    transfer1_amount = 90 # $90
    service_charge1 = (service_charge_percent_numerator / percent_denominator) * transfer1_amount

    # L2
    transfer2_amount = 60 # $60
    service_charge2 = (service_charge_percent_numerator / percent_denominator) * transfer2_amount

    # L3
    total_deducted = transfer1_amount + service_charge1 + service_charge2

    # L4
    initial_balance = 400 # $400 before he made any of the transfers
    final_balance = initial_balance - total_deducted

    # FA
    answer = final_balance
    return answer