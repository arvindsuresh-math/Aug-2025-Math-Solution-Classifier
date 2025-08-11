def solve():
    """Index: 3230.
    Returns: the difference in money Nancy will make.
    """
    # L1
    total_jade_grams = 1920 # 1920 grams of jade
    jade_per_giraffe = 120 # 120 grams of jade
    num_giraffe_statues = total_jade_grams / jade_per_giraffe

    # L2
    price_per_giraffe = 150 # sells for $150
    total_earnings_giraffes = num_giraffe_statues * price_per_giraffe

    # L3
    double_factor = 2 # twice as much jade
    jade_per_elephant = jade_per_giraffe * double_factor

    # L4
    num_elephant_statues = total_jade_grams / jade_per_elephant

    # L5
    price_per_elephant = 350 # sells for $350
    total_earnings_elephants = num_elephant_statues * price_per_elephant

    # L6
    money_difference = total_earnings_elephants - total_earnings_giraffes

    # FA
    answer = money_difference
    return answer