def solve():
    """Index: 6031.
    Returns: Sam's age.
    """
    # The problem states: "Sam and Drew have a combined age of 54. Sam is half of Drew's age."
    # Let Drew's age be x.
    # Sam's age is (1/2)x.
    # The equation is x + (1/2)x = 54, which simplifies to (3/2)x = 54, or 3x = 108.

    # L6
    combined_age = 54 # combined age of 54
    sam_fraction_of_drew = 0.5 # half of Drew's age
    drew_age = combined_age / (1 + sam_fraction_of_drew)

    # L7
    half_divisor = 2 # half of Drew's age (the divisor part)
    sam_age = drew_age / half_divisor

    # FA
    answer = sam_age
    return answer