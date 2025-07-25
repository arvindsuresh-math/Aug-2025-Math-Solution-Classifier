from fractions import Fraction

def solve():
    """Index: 3984.
    Returns: the total cost of painting the house.
    """
    # L1
    judson_contribution = 500 # Judson contributed $500
    kenny_percentage_more = Fraction(20, 100) # 20% more money than Judson
    kenny_additional_contribution = kenny_percentage_more * judson_contribution

    # L2
    kenny_total_contribution = judson_contribution + kenny_additional_contribution

    # L3
    kenny_judson_total = kenny_total_contribution + judson_contribution

    # L4
    camilo_more_than_kenny = 200 # $200 more than Kenny
    camilo_total_contribution = kenny_total_contribution + camilo_more_than_kenny

    # L5
    total_cost = kenny_judson_total + camilo_total_contribution

    # FA
    answer = total_cost
    return answer