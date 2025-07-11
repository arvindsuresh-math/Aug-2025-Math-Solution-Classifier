def solve():
    """Index: 1379.
    Returns: the total number of rabbits Lola has in her house.
    """
    # L1
    breeding_rabbits = 10 # 10 breeding rabbits
    kittens_multiplier = 10 # 10 times as many kittens as the number of breeding rabbits Lola has
    first_spring_kittens = breeding_rabbits * kittens_multiplier

    # L2
    adopted_divisor = 2 # half of the kittens got adopted
    adopted_kittens = first_spring_kittens / adopted_divisor

    # L3
    returned_kittens = 5 # 5 of them had to be returned
    kittens_after_returns = adopted_kittens + returned_kittens

    # L4
    next_spring_total_kittens = 60 # only had a total of 60 kittens
    next_spring_adopted = 4 # with 4 of the kittens being adopted
    next_spring_stayed_kittens = next_spring_total_kittens - next_spring_adopted

    # L5
    total_offspring = kittens_after_returns + next_spring_stayed_kittens

    # L6
    total_rabbits = total_offspring + breeding_rabbits

    # FA
    answer = total_rabbits
    return answer