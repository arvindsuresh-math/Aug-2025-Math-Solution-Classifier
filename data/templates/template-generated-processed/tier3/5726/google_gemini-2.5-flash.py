from fractions import Fraction

def solve():
    """Index: 5726.
    Returns: the loss Cara and Janet will make.
    """
    # L1
    cara_ratio_part = 4 # The ratio of the amount of money Cara, Janet, and Jerry have is 4:5:6
    janet_ratio_part = 5 # The ratio of the amount of money Cara, Janet, and Jerry have is 4:5:6
    jerry_ratio_part = 6 # The ratio of the amount of money Cara, Janet, and Jerry have is 4:5:6
    sum_of_ratios = cara_ratio_part + janet_ratio_part + jerry_ratio_part

    # L2
    total_money = 75 # If the total amount of money they have is $75
    cara_money_fraction = Fraction(cara_ratio_part, sum_of_ratios)
    cara_money = cara_money_fraction * total_money

    # L3
    janet_money_fraction = Fraction(janet_ratio_part, sum_of_ratios)
    janet_money = janet_money_fraction * total_money

    # L4
    combined_money = cara_money + janet_money

    # L5
    selling_percentage_numerator = 80 # sell them at 80% of the buying price
    selling_percentage_denominator = 100 # sell them at 80% of the buying price
    selling_price = Fraction(selling_percentage_numerator, selling_percentage_denominator) * combined_money

    # L6
    loss = combined_money - selling_price

    # FA
    answer = loss
    return answer