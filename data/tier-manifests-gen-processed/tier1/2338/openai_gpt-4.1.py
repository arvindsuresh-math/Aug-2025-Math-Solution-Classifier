def solve():
    """Index: 2338.
    Returns: the total number of cups of water needed to fill 10 whole bottles and 5 half-capacity bottles.
    """
    # L1
    num_whole_bottles = 10 # 10 whole bottles
    cups_per_bottle = 2 # a bottle can hold 2 cups of water
    cups_whole = num_whole_bottles * cups_per_bottle

    # L2
    num_half_bottles = 5 # 5 half-capacity bottles
    cups_per_half_bottle = 1 # half-capacity bottle holds 1 cup (half of 2 cups)
    cups_half = num_half_bottles * cups_per_half_bottle

    # L3
    total_cups = cups_whole + cups_half

    # FA
    answer = total_cups
    return answer