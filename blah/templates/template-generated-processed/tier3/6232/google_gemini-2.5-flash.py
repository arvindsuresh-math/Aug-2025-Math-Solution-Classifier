def solve():
    """Index: 6232.
    Returns: the total amount of money collected at the party.
    """
    # L1
    num_boys = 40 # 40 boys at the party
    boy_payment = 50 # each boy paid $50
    total_boy_payment = num_boys * boy_payment

    # L2
    boys_to_girls_ratio = 4 # four times as many boys
    num_girls = num_boys / boys_to_girls_ratio

    # L3
    boy_girl_payment_ratio = 2 # twice the money
    girl_payment = boy_payment / boy_girl_payment_ratio

    # L4
    total_girl_payment = girl_payment * num_girls

    # L5
    total_money_collected = total_girl_payment + total_boy_payment

    # FA
    answer = total_money_collected
    return answer