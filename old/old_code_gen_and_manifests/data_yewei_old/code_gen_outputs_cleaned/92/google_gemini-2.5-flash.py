def solve():
    # Given daily earnings
    sally_daily_earnings = 6
    bob_daily_earnings = 4

    # Savings rate (half of what they earn)
    savings_rate = 0.5

    # Number of days in a year
    days_in_year = 365

    # Calculate Sally's daily savings
    sally_daily_savings = sally_daily_earnings * savings_rate

    # Calculate Sally's annual savings
    sally_annual_savings = sally_daily_savings * days_in_year

    # Calculate Bob's daily savings
    bob_daily_savings = bob_daily_earnings * savings_rate

    # Calculate Bob's annual savings
    bob_annual_savings = bob_daily_savings * days_in_year

    # Calculate total savings for both
    total_savings = sally_annual_savings + bob_annual_savings

    return total_savings

# Execute the function to get the answer
answer = solve()