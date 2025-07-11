from fractions import Fraction

def solve():
    """Index: 1500.
    Returns: the amount of change Mr. Arevalo will receive.
    """
    # L1
    smoky_salmon_cost = 40 # The smoky salmon costs $40
    black_burger_cost = 15 # the black burger costs $15
    chicken_katsu_cost = 25 # and the chicken katsu costs $25
    food_total_cost = smoky_salmon_cost + black_burger_cost + chicken_katsu_cost

    # L2
    service_charge_percentage = Fraction(10, 100) # a 10% service charge
    service_charge_amount = food_total_cost * service_charge_percentage

    # L3
    tip_percentage = Fraction(5, 100) # and 5% tip
    tip_amount = food_total_cost * tip_percentage

    # L4
    total_bill = food_total_cost + service_charge_amount + tip_amount

    # L5
    amount_paid = 100 # from his $100
    change_received = amount_paid - total_bill

    # FA
    answer = change_received
    return answer