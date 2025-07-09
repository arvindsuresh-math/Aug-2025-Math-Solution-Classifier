def solve_36():
    """
    Calculates how much more money Lisa earned than Tommy based on the given conditions.
    """
    total_earnings = 60  # Total money earned from washing cars

    # Lisa earned half of the total earnings
    lisa_earnings = total_earnings / 2

    # Tommy earned half of what Lisa earned
    tommy_earnings = lisa_earnings / 2

    # Calculate how much more Lisa earned than Tommy
    difference = lisa_earnings - tommy_earnings

    return difference

# Execute the function to get the answer
answer = solve_36()