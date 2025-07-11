def solve():
    """Index: 1850.
    Returns: the number of extra square feet the leftover grass seed could cover.
    """
    # L1
    lawn_length = 22 # 22 feet from the house to the curb
    lawn_width = 36 # 36 feet from side to side
    lawn_area = lawn_length * lawn_width

    # L2
    covers_per_bag = 250 # One bag of grass seed covers 250 square feet
    bags_bought = 4 # He bought four bags of seed
    total_coverage = covers_per_bag * bags_bought

    # L3
    leftover_coverage = total_coverage - lawn_area

    # FA
    answer = leftover_coverage
    return answer