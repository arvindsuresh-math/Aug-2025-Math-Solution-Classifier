def solve():
    """Index: 7377.
    Returns: the amount Darrel will receive after the 10% fee.
    """
    # L1
    num_quarters = 76 # 76 quarters
    value_quarter = 0.25 # WK
    quarters_value = num_quarters * value_quarter

    # L2
    num_dimes = 85 # 85 dimes
    value_dime = 0.10 # WK
    dimes_value = num_dimes * value_dime

    # L3
    num_nickels = 20 # 20 nickels
    value_nickel = 0.05 # WK
    nickels_value = num_nickels * value_nickel

    # L4
    num_pennies = 150 # 150 pennies
    value_penny = 0.01 # WK
    pennies_value = num_pennies * value_penny

    # L5
    total_money_before_fee = quarters_value + dimes_value + nickels_value + pennies_value

    # L6
    fee_percent_text = 10 # 10% fee
    fee_percent_decimal = 0.10 # 10% fee
    fee_amount = fee_percent_decimal * total_money_before_fee

    # L7
    money_after_fee = total_money_before_fee - fee_amount

    # FA
    answer = money_after_fee
    return answer