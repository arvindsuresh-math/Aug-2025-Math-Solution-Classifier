def solve():
    """Index: 1731.
    Returns: how much farther Margarita ran and jumped than Ricciana.
    """
    # L1
    ricciana_jump = 4 # Ricciana ... jumped a total of 24 feet - 20 feet for running and 4 feet for jumping
    twice = 2 # twice Ricciana's jump
    twice_ricciana_jump = ricciana_jump * twice

    # L2
    less_than_twice = 1 # jumped 1 foot less than twice Ricciana's jump
    margarita_jump = twice_ricciana_jump - less_than_twice

    # L3
    margarita_run = 18 # Margarita ran for 18 feet
    margarita_total = margarita_run + margarita_jump

    # L4
    ricciana_total = 24 # Ricciana ran and jumped a total of 24 feet
    difference = margarita_total - ricciana_total

    # FA
    answer = difference
    return answer