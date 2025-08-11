def solve():
    """Index: 4786.
    Returns: the difference in eggs needed for cheesecakes vs. chocolate cakes.
    """
    # L1
    eggs_per_cheesecake = 8 # 8 eggs for each cheesecake
    num_cheesecakes = 9 # 9 cheesecakes
    total_eggs_cheesecakes = eggs_per_cheesecake * num_cheesecakes

    # L2
    num_chocolate_cakes = 5 # 5 chocolate cakes
    eggs_per_chocolate_cake = 3 # 3 eggs per cake
    total_eggs_chocolate_cakes = num_chocolate_cakes * eggs_per_chocolate_cake

    # L3
    egg_difference = total_eggs_cheesecakes - total_eggs_chocolate_cakes

    # FA
    answer = egg_difference
    return answer