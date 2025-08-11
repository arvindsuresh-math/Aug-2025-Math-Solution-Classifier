from fractions import Fraction

def solve():
    """Index: 6882.
    Returns: the total amount of remaining money at the end of the month.
    """
    # L1
    debit_card_fraction = Fraction(1, 2) # half of his pay
    total_pay = 5000 # In June, he earned $5000
    debit_card_recharge = debit_card_fraction * total_pay

    # L2
    car_cost = 1500 # bought himself a used car worth $1500
    remaining_money = debit_card_recharge - car_cost

    # FA
    answer = remaining_money
    return answer