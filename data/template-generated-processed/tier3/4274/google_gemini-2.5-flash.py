from fractions import Fraction

def solve():
    """Index: 4274.
    Returns: the total amount Mr. Eithan kept in the family's savings account.
    """
    # L1
    stimulus_check_amount = 2000 # the $2000 stimulus check
    wife_fraction = Fraction(2, 5) # 2/5 of the amount to his wife
    amount_to_wife = wife_fraction * stimulus_check_amount

    # L2
    remaining_after_wife = stimulus_check_amount - amount_to_wife

    # L3
    first_son_fraction = Fraction(2, 5) # 2/5 of the remaining amount to his first son
    amount_to_first_son = first_son_fraction * remaining_after_wife

    # L4
    remaining_after_first_son = remaining_after_wife - amount_to_first_son

    # L5
    second_son_percentage = Fraction(40, 100) # 40% of the remaining amount to his second son
    amount_to_second_son = second_son_percentage * remaining_after_first_son

    # L6
    amount_in_savings = remaining_after_first_son - amount_to_second_son

    # FA
    answer = amount_in_savings
    return answer