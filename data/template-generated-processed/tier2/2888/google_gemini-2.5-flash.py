def solve():
    """Index: 2888.
    Returns: the total amount saved by buying chlorine and soap.
    """
    # L1
    chlorine_cost_per_liter = 10 # A liter of chlorine costs $10
    chlorine_discount_percent = 0.20 # sold at 20% off
    chlorine_saving_per_liter = chlorine_cost_per_liter * chlorine_discount_percent

    # L2
    soap_cost_per_box = 16 # A box of soap that costs $16
    soap_discount_percent = 0.25 # sold at 25% off
    soap_saving_per_box = soap_cost_per_box * soap_discount_percent

    # L3
    num_liters_chlorine = 3 # buy 3 liters of chlorine
    total_chlorine_saving = chlorine_saving_per_liter * num_liters_chlorine

    # L4
    num_boxes_soap = 5 # 5 boxes of soap
    total_soap_saving = soap_saving_per_box * num_boxes_soap

    # L5
    total_saving = total_chlorine_saving + total_soap_saving

    # FA
    answer = total_saving
    return answer