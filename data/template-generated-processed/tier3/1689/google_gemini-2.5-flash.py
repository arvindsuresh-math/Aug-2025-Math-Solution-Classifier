from fractions import Fraction

def solve():
    """Index: 1689.
    Returns: the total amount of money Baylor will have in his dashboard.
    """
    # L1
    initial_dashboard_money = 4000 # Currently, he has $4000 on his dashboard
    first_client_fraction = Fraction(1, 2) # half the amount
    first_client_denominator_for_calc = 2 # half the amount
    first_client_payment = first_client_fraction * initial_dashboard_money

    # L2
    second_client_fraction = Fraction(2, 5) # 2/5 times more money
    additional_second_client_payment = second_client_fraction * first_client_payment

    # L3
    total_second_client_payment = first_client_payment + additional_second_client_payment

    # L4
    first_and_second_clients_total = total_second_client_payment + first_client_payment

    # L5
    third_client_multiplier = 2 # twice the amount
    third_client_payment = third_client_multiplier * first_and_second_clients_total

    # L6
    total_clients_payment = third_client_payment + first_and_second_clients_total

    # L7
    final_dashboard_money = total_clients_payment + initial_dashboard_money

    # FA
    answer = final_dashboard_money
    return answer