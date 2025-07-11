def solve():
    """Index: 1980.
    Returns: the number of balloons left after some burst.
    """
    # L1
    num_bags_round = 5 # 5 bags of round balloons
    balloons_per_bag_round = 20 # 20 balloons in each bag
    total_round = num_bags_round * balloons_per_bag_round

    # L2
    num_bags_long = 4 # 4 bags of long balloons
    balloons_per_bag_long = 30 # 30 balloons in each bag
    total_long = num_bags_long * balloons_per_bag_long

    # L3
    total_balloons = total_round + total_long

    # L4
    round_burst = 5 # 5 round balloons burst
    balloons_left = total_balloons - round_burst

    # FA
    answer = balloons_left
    return answer