def solve():
    """Index: 6312.
    Returns: the number of apples Tom has.
    """
    # L1
    phillip_apples = 40 # Phillip has 40 apples
    ben_more_than_phillip = 8 # Ben has 8 apples more than Phillip does
    ben_apples = phillip_apples + ben_more_than_phillip

    # L2
    eighth_denominator = 8 # three eighths as many apples
    apples_per_eighth = ben_apples / eighth_denominator

    # L3
    eighth_numerator = 3 # three eighths as many apples
    tom_apples = apples_per_eighth * eighth_numerator

    # FA
    answer = tom_apples
    return answer