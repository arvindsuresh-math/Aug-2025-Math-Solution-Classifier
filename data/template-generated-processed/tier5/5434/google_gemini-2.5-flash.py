def solve():
    """Index: 5434.
    Returns: the number of apples Kayla picked.
    """
    # L6
    total_apples = 340 # 340 apples total
    kayla_additional = 10 # 10 more
    kayla_multiplier = 4 # 4 times
    # The solution implicitly solves the equation: total_apples = x + (kayla_additional + kayla_multiplier * x)
    # Which simplifies to: total_apples = (1 + kayla_multiplier) * x + kayla_additional
    # Rearranging: total_apples - kayla_additional = (1 + kayla_multiplier) * x
    # Solving for x: x = (total_apples - kayla_additional) / (1 + kayla_multiplier)
    kylie_apples = (total_apples - kayla_additional) / (1 + kayla_multiplier)

    # L7
    kayla_apples = kayla_additional + kayla_multiplier * kylie_apples

    # FA
    answer = kayla_apples
    return answer