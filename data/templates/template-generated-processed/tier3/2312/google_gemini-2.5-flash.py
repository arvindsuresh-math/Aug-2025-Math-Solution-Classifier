from fractions import Fraction

def solve():
    """Index: 2312.
    Returns: the total price of the gift Lisa wanted to buy.
    """
    # L1
    saved_amount = 1200 # Lisa has saved $1200
    mother_fraction = Fraction(3, 5) # her mother gave her 3/5 times of what she had saved
    mother_contribution = mother_fraction * saved_amount

    # L2
    brother_multiplier = 2 # her brother gave her twice the amount her mother gave her
    brother_contribution = brother_multiplier * mother_contribution

    # L3
    remaining_needed = 400 # she still had $400 less
    gift_price = saved_amount + brother_contribution + mother_contribution + remaining_needed

    # FA
    answer = gift_price
    return answer