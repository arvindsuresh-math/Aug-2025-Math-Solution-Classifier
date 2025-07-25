def solve():
    """Index: 6432.
    Returns: the difference in money between Mary and Marco.
    """
    # L1
    marco_initial_money = 24 # Marco has $24
    half_divisor = 2 # half of what he has
    marco_half_money = marco_initial_money / half_divisor

    # L2
    mary_initial_money = 15 # Mary has $15
    mary_money_after_receiving = marco_half_money + mary_initial_money

    # L3
    mary_spends = 5 # Mary spends $5
    mary_money_after_spending = mary_money_after_receiving - mary_spends

    # L4
    difference_in_money = mary_money_after_spending - marco_half_money

    # FA
    answer = difference_in_money
    return answer