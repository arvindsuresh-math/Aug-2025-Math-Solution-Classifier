def solve():
    """Index: 953.
    Returns: the total number of chickens Wendi has.
    """
    # L1
    initial_chickens = 4 # Wendi brought home 4 chickens
    double_factor = 2 # double the number of chickens
    chickens_after_doubling = initial_chickens * double_factor

    # L2
    dog_ate = 1 # dog ate one of her chickens
    chickens_after_dog = chickens_after_doubling - dog_ate

    # L3
    ten_chickens = 10 # ten chickens
    less_than_ten = 4 # 4 less than ten chickens
    additional_chickens_found = ten_chickens - less_than_ten

    # L4
    final_chickens = chickens_after_dog + additional_chickens_found

    # FA
    answer = final_chickens
    return answer