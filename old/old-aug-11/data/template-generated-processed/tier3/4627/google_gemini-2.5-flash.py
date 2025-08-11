from fractions import Fraction

def solve():
    """Index: 4627.
    Returns: the remaining money Asha has.
    """
    # L1
    borrowed_brother = 20 # borrow $20 from her brother
    borrowed_father = 40 # $40 from her father
    borrowed_mother = 30 # $30 from her mother
    total_borrowed = borrowed_brother + borrowed_father + borrowed_mother

    # L2
    gifted_granny = 70 # gifted $70 by her granny
    total_after_granny_gift = gifted_granny + total_borrowed

    # L3
    initial_savings = 100 # her savings of $100
    total_money_before_spending = total_after_granny_gift + initial_savings

    # L4
    spent_fraction = Fraction(3, 4) # spent 3/4 of the money
    money_spent = spent_fraction * total_money_before_spending

    # L5
    remaining_money = total_money_before_spending - money_spent

    # FA
    answer = remaining_money
    return answer