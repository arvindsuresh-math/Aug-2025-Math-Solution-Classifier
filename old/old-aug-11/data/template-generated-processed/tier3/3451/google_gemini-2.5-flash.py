from fractions import Fraction

def solve():
    """Index: 3451.
    Returns: the total remaining weight of the stock.
    """
    # L1
    green_beans_weight = 60 # If the green beans weighed 60 kgs
    rice_less_than_beans = 30 # rice weighing 30 kg less than green beans
    rice_weight = green_beans_weight - rice_less_than_beans

    # L2
    beans_more_than_sugar = 10 # 10 kg more than sugar
    sugar_weight = green_beans_weight - beans_more_than_sugar

    # L3
    rice_loss_fraction = Fraction(1, 3) # 1/3 weight of the rice
    lost_rice_weight = rice_loss_fraction * rice_weight

    # L4
    remaining_rice_weight = rice_weight - lost_rice_weight

    # L5
    sugar_loss_fraction = Fraction(1, 5) # 1/5 weight of sugar
    lost_sugar_weight = sugar_loss_fraction * sugar_weight

    # L6
    remaining_sugar_weight = sugar_weight - lost_sugar_weight

    # L7
    total_remaining_stock_weight = remaining_sugar_weight + remaining_rice_weight + green_beans_weight

    # FA
    answer = total_remaining_stock_weight
    return answer