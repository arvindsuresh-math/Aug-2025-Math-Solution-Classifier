def solve():
    """Index: 4784.
    Returns: the total population of the three animals in the park.
    """
    # L1
    lions_count = 200 # number of lions is 200
    leopard_ratio_divisor = 2 # twice the number of leopards
    leopards_count = lions_count / leopard_ratio_divisor

    # L2
    lions_and_leopards_total = lions_count + leopards_count

    # L3
    elephant_ratio_divisor = 2 # half the combined number of lions and leopards
    elephants_count = lions_and_leopards_total / elephant_ratio_divisor

    # L4
    total_animals = elephants_count + lions_and_leopards_total

    # FA
    answer = total_animals
    return answer