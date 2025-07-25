from fractions import Fraction

def solve():
    """Index: 202.
    Returns: the total amount of money in Susie's piggy bank.
    """
    # L1
    percentage_increase = Fraction(20, 100) # 20% more money
    initial_money = 200 # $200 in her piggy bank
    additional_money = percentage_increase * initial_money

    # L2
    total_money = initial_money + additional_money

    # FA
    answer = total_money
    return answer