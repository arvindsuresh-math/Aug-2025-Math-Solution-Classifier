from fractions import Fraction

def solve():
    """Index: 202.
    Returns: the total amount of money Susie will have in her piggy bank after adding 20% more.
    """
    # L1
    percent_increase = Fraction(20, 100) # 20% more money
    initial_amount = 200 # $200 in her piggy bank
    additional_amount = percent_increase * initial_amount

    # L2
    total_amount = initial_amount + additional_amount

    # FA
    answer = total_amount
    return answer