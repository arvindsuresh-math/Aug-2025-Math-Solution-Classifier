def solve():
    """
    Calculates the total amount of money shared by Mr. Sam between his two sons.

    Ken's share is given. Tony's share is twice Ken's share.
    The total shared amount is the sum of Ken's and Tony's shares.
    """
    ken_share = 1750  # Amount Ken received in dollars
    
    # Calculate Tony's share, which is twice Ken's share
    tony_share = 2 * ken_share
    
    # Calculate the total amount of money shared
    total_shared_money = ken_share + tony_share
    
    return total_shared_money

# Execute the function to get the answer
answer = solve()