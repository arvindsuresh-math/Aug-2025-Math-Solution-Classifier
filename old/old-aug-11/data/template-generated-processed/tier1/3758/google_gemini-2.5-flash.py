def solve():
    """Index: 3758.
    Returns: the profit made in the second quarter.
    """
    # L1
    profit_q1 = 1500 # profits of $1,500 in the first quarter
    profit_q3 = 3000 # $3,000 in the third quarter
    profit_q4 = 2000 # $2,000 in the fourth quarter
    profit_three_quarters = profit_q1 + profit_q3 + profit_q4

    # L2
    annual_profit = 8000 # annual profits are $8,000
    profit_q2 = annual_profit - profit_three_quarters

    # FA
    answer = profit_q2
    return answer