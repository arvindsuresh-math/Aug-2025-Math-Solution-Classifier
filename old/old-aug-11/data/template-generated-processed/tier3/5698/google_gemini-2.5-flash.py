def solve():
    """Index: 5698.
    Returns: the number of weeks Daria needs to raise enough money.
    """
    # L1
    vacuum_cost = 120 # The vacuum cleaner costs $120
    initial_collected = 20 # collected $20 in her piggy bank
    money_needed = vacuum_cost - initial_collected

    # L2
    weekly_contribution = 10 # put $10 in it each week
    weeks_needed = money_needed / weekly_contribution

    # FA
    answer = weeks_needed
    return answer