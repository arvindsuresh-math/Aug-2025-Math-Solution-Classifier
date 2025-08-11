def solve():
    """Index: 4358.
    Returns: the number of slices each pizza should be divided into.
    """
    # L1
    num_pizzas = 5 # After buying 5 pizzas
    slices_option1 = 6 # divide each pizza into either 6
    total_slices_option1 = num_pizzas * slices_option1
    slices_option2 = 8 # 8
    total_slices_option2 = num_pizzas * slices_option2
    slices_option3 = 10 # or 10 slices
    total_slices_option3 = num_pizzas * slices_option3

    # L3
    num_children = 20 # There are a total of 20 children at the party
    slices_per_child_option2 = total_slices_option2 / num_children

    # FA
    answer = slices_option2
    return answer