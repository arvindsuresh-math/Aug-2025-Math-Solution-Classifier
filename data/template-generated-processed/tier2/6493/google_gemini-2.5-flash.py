def solve():
    """Index: 6493.
    Returns: the number of scoops Michael should remove.
    """
    # L1
    total_flour_in_bag = 8 # 8 cup bag of flour
    flour_needed = 6 # needs 6 cups of flour
    flour_to_remove = total_flour_in_bag - flour_needed

    # L2
    measuring_cup_size = 0.25 # 1/4 cup
    num_scoops = flour_to_remove / measuring_cup_size

    # FA
    answer = num_scoops
    return answer