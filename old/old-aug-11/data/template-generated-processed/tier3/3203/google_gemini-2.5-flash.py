from fractions import Fraction

def solve():
    """Index: 3203.
    Returns: the cost of transporting the new quantity of cement bags.
    """
    # L1
    initial_bags = 80 # 80 bags of cement
    bag_multiplier = 3 # three times as many cement bags
    new_bags = bag_multiplier * initial_bags

    # L2
    initial_weight_per_bag = 50 # each weighing 50 kgs
    weight_multiplier = Fraction(3, 5) # 3/5 times as many kgs
    new_weight_per_bag = weight_multiplier * initial_weight_per_bag

    # L3
    initial_cost = 6000 # cost of transporting ... is $6000
    cost_per_initial_bag = initial_cost / initial_bags

    # L4
    cost_per_new_bag = new_weight_per_bag * cost_per_initial_bag / initial_weight_per_bag

    # L5
    total_new_cost = cost_per_new_bag * new_bags

    # FA
    answer = total_new_cost
    return answer