from fractions import Fraction

def solve():
    """Index: 3774.
    Returns: the combined weight of both Oliver's bags.
    """
    # L1
    james_bag_weight = 18 # James’s bag, which weighs 18kg
    fraction_of_james_bag = Fraction(1, 6) # 1/6 as much as James’s bag
    oliver_single_bag_weight = james_bag_weight * fraction_of_james_bag

    # L2
    number_of_bags = 2 # two bags of vegetables
    combined_weight = oliver_single_bag_weight * number_of_bags

    # FA
    answer = combined_weight
    return answer