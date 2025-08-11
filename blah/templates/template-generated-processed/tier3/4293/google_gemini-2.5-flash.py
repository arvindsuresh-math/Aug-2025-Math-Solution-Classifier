from fractions import Fraction

def solve():
    """Index: 4293.
    Returns: the total amount of money Prince spent on buying the CDs.
    """
    # L1
    percentage_10_dollar_cds = Fraction(40, 100) # 40% of the CDs
    total_cds = 200 # total number of CDs was 200
    num_10_dollar_cds = percentage_10_dollar_cds * total_cds

    # L2
    num_5_dollar_cds = total_cds - num_10_dollar_cds

    # L3
    prince_bought_10_dollar_fraction = Fraction(1, 2) # half the CDs sold at $10 each
    prince_num_10_dollar_cds = prince_bought_10_dollar_fraction * num_10_dollar_cds

    # L4
    cost_10_dollar_cd = 10 # $10 each
    cost_prince_10_dollar_cds = prince_num_10_dollar_cds * cost_10_dollar_cd

    # L5
    cost_5_dollar_cd = 5 # $5 each
    cost_prince_5_dollar_cds = cost_5_dollar_cd * num_5_dollar_cds

    # L6
    total_spent = cost_prince_5_dollar_cds + cost_prince_10_dollar_cds

    # FA
    answer = total_spent
    return answer