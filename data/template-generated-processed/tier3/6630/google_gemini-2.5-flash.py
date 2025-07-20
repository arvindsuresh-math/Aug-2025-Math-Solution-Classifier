from fractions import Fraction

def solve():
    """Index: 6630.
    Returns: the amount of money that goes to the contingency fund.
    """
    # L1
    total_donation = 240 # $240 to a private organization
    community_pantry_fraction = Fraction(1, 3) # 1/3 of it goes to the community pantry project
    community_pantry_amount = total_donation * community_pantry_fraction

    # L2
    local_crisis_fraction = Fraction(1, 2) # 1/2 goes to the local crisis fund
    local_crisis_amount = total_donation * local_crisis_fraction

    # L3
    allocated_for_two_funds = community_pantry_amount + local_crisis_amount

    # L4
    remaining_funds_for_other_two = total_donation - allocated_for_two_funds

    # L5
    livelihood_fraction = Fraction(1, 4) # 1/4 of the remaining goes to livelihood project funds
    livelihood_project_amount = remaining_funds_for_other_two * livelihood_fraction

    # L6
    contingency_fund_amount = remaining_funds_for_other_two - livelihood_project_amount

    # FA
    answer = contingency_fund_amount
    return answer