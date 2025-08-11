from fractions import Fraction

def solve():
    """Index: 3194.
    Returns: the difference in the number of married people and children.
    """
    # L1
    total_guests = 1000 # 1000 guests
    married_percentage = Fraction(30, 100) # 30% of the guests are married
    married_guests = total_guests * married_percentage

    # L2
    single_percentage = Fraction(50, 100) # 50% are single
    single_guests = total_guests * single_percentage

    # L3
    married_and_single_guests = married_guests + single_guests

    # L4
    children_guests = total_guests - married_and_single_guests

    # L5
    difference_married_children = married_guests - children_guests

    # FA
    answer = difference_married_children
    return answer