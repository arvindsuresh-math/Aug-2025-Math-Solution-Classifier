def solve():
    """Index: 6206.
    Returns: the difference in money Frank will spend compared to Eman.
    """
    # L1
    joystick_cost = 20 # joystick costs $20
    frank_joystick_fraction_numerator = 1 # 1/4 of the price of the joystick
    frank_joystick_fraction_denominator = 4 # 1/4 of the price of the joystick
    frank_joystick_payment = joystick_cost * frank_joystick_fraction_numerator / frank_joystick_fraction_denominator

    # L2
    eman_joystick_payment = joystick_cost - frank_joystick_payment

    # L3
    computer_table_cost = 140 # computer table costs $140
    frank_total_payment = computer_table_cost + frank_joystick_payment

    # L4
    computer_chair_cost = 100 # computer chair costs $100
    eman_total_payment = computer_chair_cost + eman_joystick_payment

    # L5
    difference_in_spending = frank_total_payment - eman_total_payment

    # FA
    answer = difference_in_spending
    return answer