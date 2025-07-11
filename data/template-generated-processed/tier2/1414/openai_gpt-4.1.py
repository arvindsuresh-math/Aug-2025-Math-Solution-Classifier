def solve():
    """Index: 1414.
    Returns: the final cost of the medicine after cashback and rebate offers.
    """
    # L1
    cashback_percent_decimal = 0.10 # .10*150 from solution text
    cashback_percent_num = 10 # 10% cashback
    percent_factor = 0.01 # WK
    medicine_cost = 150.00 # $150.00 online
    cashback_amount = cashback_percent_num * percent_factor * medicine_cost

    # L2
    rebate_amount = 25.00 # $25.00 mail-in rebate
    total_discounts = cashback_amount + rebate_amount

    # L3
    final_cost = medicine_cost - total_discounts

    # FA
    answer = final_cost
    return answer