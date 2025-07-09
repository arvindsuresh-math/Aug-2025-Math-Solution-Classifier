def solve():
    """
    Calculates the total number of geckos Brandon sold in the last two years.
    """
    geckos_last_year = 86
    
    # Calculate geckos sold the year before (twice last year's amount)
    geckos_year_before = geckos_last_year * 2
    
    # Calculate the total geckos sold in the last two years
    total_geckos_sold = geckos_last_year + geckos_year_before
    
    return total_geckos_sold

# Execute the function to get the answer
answer = solve()