def solve():
    """Index: 7090.
    Returns: the number of berries Stacy has.
    """
    # L1: "Let x be the number of berries Skylar has." - This line defines a variable 'x' but does not involve a numerical computation or calculator annotation, so it is omitted from the function code.

    # L2
    steve_multiplier = 2 # double the number of berries that Skylar has
    steve_expression = steve_multiplier

    # L3
    stacy_multiplier_factor = 4 # 4 times as many berries as Steve
    stacy_expression = stacy_multiplier_factor * steve_expression

    # L4: "1100=x+2x+8x" - This line sets up the equation but does not involve a numerical computation or calculator annotation, so it is omitted from the function code.
    total_berries = 1100 # 1100 berries total

    # L5
    # The sum of coefficients for x: 1 (for Skylar) + 2 (for Steve) + 8 (for Stacy)
    total_x_coefficient = 1 + steve_expression + stacy_expression

    # L6
    skylar_berries = total_berries / total_x_coefficient
    skylar_berries_calculated = skylar_berries # This variable is used to match the '100=100' format in the solution template.

    # L7
    stacy_actual_berries = stacy_expression * skylar_berries

    # FA
    answer = stacy_actual_berries
    return answer