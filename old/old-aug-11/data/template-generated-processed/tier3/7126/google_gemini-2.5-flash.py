def solve():
    """Index: 7126.
    Returns: the total amount Hannah paid for the appliances after the discount.
    """
    # L1
    washing_machine_cost = 100 # Hannah bought a new washing machine for $100
    dryer_cost_difference = 30 # a dryer that costs $30 less
    dryer_cost = washing_machine_cost - dryer_cost_difference

    # L2
    total_cost_before_discount = washing_machine_cost + dryer_cost

    # L3
    discount_percentage_numerator = 10 # a 10% discount
    discount_percentage_denominator = 100 # a 10% discount
    discount_amount = total_cost_before_discount * discount_percentage_numerator / discount_percentage_denominator

    # L4
    final_payment = total_cost_before_discount - discount_amount

    # FA
    answer = final_payment
    return answer