def solve():
    """Index: 992.
    Returns: the number of cups of flour Hannah should use.
    """
    # L1
    total_bananas_used = 20 # If Hannah uses 20 bananas
    bananas_per_cup_mush = 4 # 4 bananas to make one cup of mush
    cups_of_banana_mush = total_bananas_used / bananas_per_cup_mush

    # L2
    flour_per_cup_mush = 3 # 3 cups of flour for every cup of banana mush
    cups_of_flour = cups_of_banana_mush * flour_per_cup_mush

    # FA
    answer = cups_of_flour
    return answer