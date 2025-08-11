def solve():
    """Index: 4897.
    Returns: the number of green fish in the aquarium.
    """
    # L1
    total_fish = 80 # total number of fish in the aquarium is 80
    blue_fish_divisor = 2 # Blue fish make up half of all the fish
    blue_fish = total_fish / blue_fish_divisor

    # L2
    orange_fish_difference = 15 # 15 fewer orange fish
    orange_fish = blue_fish - orange_fish_difference

    # L3
    green_fish = total_fish - orange_fish - blue_fish

    # FA
    answer = green_fish
    return answer