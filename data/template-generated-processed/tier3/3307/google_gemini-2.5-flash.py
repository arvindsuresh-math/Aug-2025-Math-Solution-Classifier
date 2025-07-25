from fractions import Fraction

def solve():
    """Index: 3307.
    Returns: the profit made from selling the goods.
    """
    # L1
    natasha_money = 60 # Natasha has $60
    natasha_carla_multiplier = 3 # 3 times as much money as Carla
    carla_money = natasha_money / natasha_carla_multiplier

    # L2
    carla_natasha_total = carla_money + natasha_money

    # L3
    carla_cosima_multiplier = 2 # twice as much money as Cosima
    cosima_money = carla_money / carla_cosima_multiplier

    # L4
    total_money_initial = cosima_money + carla_natasha_total

    # L5
    selling_price_fraction = Fraction(7, 5) # 7/5 of the buying price
    total_selling_price = selling_price_fraction * total_money_initial

    # L6
    profit = total_selling_price - total_money_initial

    # FA
    answer = profit
    return answer