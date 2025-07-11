from fractions import Fraction

def solve():
    """Index: 483.
    Returns: how much less Andy weighs now than at the beginning of the year.
    """
    # L1
    initial_weight = 156 # Andy started out the year weighing 156 pounds
    weight_gain = 36 # gained 36 pounds
    post_growth_weight = initial_weight + weight_gain

    # L2
    weight_loss_fraction = Fraction(1, 8) # lost an eighth of his weight every month
    one_month_loss = weight_loss_fraction * post_growth_weight

    # L3
    months = 3 # over the next 3 months
    total_loss = one_month_loss * months

    # L4
    final_weight = post_growth_weight - total_loss

    # L5
    weight_difference = initial_weight - final_weight

    # FA
    answer = weight_difference
    return answer