def solve():
    """Index: 4551.
    Returns: the number of flowers Lilly can buy.
    """
    # L1
    days_until_birthday = 22 # Maria's birthday is in 22 days
    savings_per_day = 2 # she saves $2 each day
    total_savings = days_until_birthday * savings_per_day

    # L2
    cost_per_flower = 4 # If a flower costs $4
    num_flowers = total_savings / cost_per_flower

    # FA
    answer = num_flowers
    return answer