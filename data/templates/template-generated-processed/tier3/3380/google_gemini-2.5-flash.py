from fractions import Fraction

def solve():
    """Index: 3380.
    Returns: the total reduction from the original selling price.
    """
    # L1
    original_price = 500 # A bag was originally priced at $500
    first_reduction_percentage = Fraction(5, 100) # the price was reduced by 5%
    first_reduction_amount = original_price * first_reduction_percentage

    # L2
    price_after_first_reduction = original_price - first_reduction_amount

    # L3
    second_reduction_percentage = Fraction(4, 100) # the selling price was reduced by 4%
    second_reduction_amount = price_after_first_reduction * second_reduction_percentage

    # L4
    final_selling_price = price_after_first_reduction - second_reduction_amount

    # L5
    total_reduction = original_price - final_selling_price

    # FA
    answer = total_reduction
    return answer