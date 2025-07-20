def solve():
    """Index: 6440.
    Returns: the total savings for the team with the group discount.
    """
    # L1
    regular_shirt_cost = 7.50 # A shirt costs $7.50
    regular_pants_cost = 15 # a pair of pants cost $15
    regular_socks_cost = 4.50 # socks cost $4.50
    regular_uniform_cost = regular_shirt_cost + regular_pants_cost + regular_socks_cost

    # L2
    discounted_shirt_cost = 6.75 # A discounted shirt cost $6.75
    discounted_pants_cost = 13.50 # a discounted pair of pants cost $13.50
    discounted_socks_cost = 3.75 # discounted socks cost $3.75
    discounted_uniform_cost = discounted_shirt_cost + discounted_pants_cost + discounted_socks_cost

    # L3
    savings_per_member = regular_uniform_cost - discounted_uniform_cost

    # L4
    num_team_members = 12 # team of 12
    total_savings = savings_per_member * num_team_members

    # FA
    answer = total_savings
    return answer