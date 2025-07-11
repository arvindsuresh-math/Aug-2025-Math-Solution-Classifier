def solve():
    """Index: 1414.
    Returns: the final cost of the medicine after cash back and rebate offers.
    """
    # L1
    initial_cost = 150.00 # $150.00 online
    cashback_percent_num = 10 # 10% cashback
    cashback_percent_decimal = 0.10 # from solution text: .10*150
    percent_factor = 0.01 # WK
    cashback_amount = cashback_percent_num * percent_factor * initial_cost

    # L2
    mail_in_rebate = 25.00 # $25.00 mail-in rebate
    cashback_amount_int = 15 # derived from cashback_amount for sum
    mail_in_rebate_int = 25 # derived from mail_in_rebate for sum
    total_discounts = cashback_amount_int + mail_in_rebate_int

    # L3
    initial_cost_int = 150 # derived from initial_cost for subtraction
    total_discounts_int = 40 # derived from total_discounts for subtraction
    final_cost = initial_cost_int - total_discounts_int

    # FA
    answer = final_cost
    return answer