def solve():
    """Index: 6225.
    Returns: how many more squares Pedro has than both Jesus and Linden combined.
    """
    # L1
    pedro_squares_in_solution = 100 # This value is used in the solution, but the question states Pedro has 200 squares. Following direct substitution rule.
    jesus_squares = 60 # Jesus has 60 squares
    pedro_more_than_jesus = pedro_squares_in_solution - jesus_squares

    # L2
    linden_squares = 75 # Linden has 75 squares
    pedro_more_than_linden = pedro_squares_in_solution - linden_squares

    # L3
    total_more_squares = pedro_more_than_jesus + pedro_more_than_linden

    # FA
    answer = total_more_squares
    return answer