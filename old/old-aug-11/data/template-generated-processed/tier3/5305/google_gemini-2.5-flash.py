from fractions import Fraction

def solve():
    """Index: 5305.
    Returns: the total amount Natalie paid for her shopping.
    """
    # L1
    apple_pie_cost = 12 # apple pie cost $12
    cheaper_percentage = Fraction(25, 100) # only 25% cheaper than the apple pie
    cheesecake_discount_amount = cheaper_percentage * apple_pie_cost

    # L2
    one_cheesecake_cost = apple_pie_cost - cheesecake_discount_amount

    # L3
    muffin_multiplier = 2 # two times more expensive than the cheesecake
    muffin_six_pack_cost = one_cheesecake_cost * muffin_multiplier

    # L4
    num_cheesecakes = 2 # two cheesecakes
    two_cheesecakes_cost = one_cheesecake_cost * num_cheesecakes

    # L5
    total_shopping_cost = muffin_six_pack_cost + two_cheesecakes_cost + apple_pie_cost

    # FA
    answer = total_shopping_cost
    return answer