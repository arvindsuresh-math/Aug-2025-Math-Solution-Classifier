def solve():
    """Index: 2888.
    Returns: the total amount saved by buying 3 liters of chlorine and 5 boxes of soap at discount.
    """
    # L1
    chlorine_price = 10 # A liter of chlorine costs $10
    chlorine_discount_decimal = 0.20 # 20% off
    chlorine_savings_per_liter = chlorine_price * chlorine_discount_decimal

    # L2
    soap_price = 16 # box of soap costs $16
    soap_discount_decimal = 0.25 # 25% off
    soap_savings_per_box = soap_price * soap_discount_decimal

    # L3
    num_chlorine = 3 # 3 liters of chlorine
    total_chlorine_savings = num_chlorine * chlorine_savings_per_liter

    # L4
    num_soap = 5 # 5 boxes of soap
    total_soap_savings = soap_savings_per_box * num_soap

    # L5
    total_savings = total_chlorine_savings + total_soap_savings

    # FA
    answer = total_savings
    return answer