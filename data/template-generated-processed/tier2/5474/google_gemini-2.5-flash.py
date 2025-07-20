def solve():
    """Index: 5474.
    Returns: the number of claims Missy can handle.
    """
    # L1
    john_percent_increase_num = 30 # 30% more claims than Jan
    jan_claims = 20 # Jan can handle 20 claims
    percent_factor = 0.01 # WK
    john_additional_claims = john_percent_increase_num * percent_factor * jan_claims

    # L2
    john_total_claims = jan_claims + john_additional_claims

    # L3
    missy_additional_claims = 15 # 15 more claims than John
    missy_total_claims = john_total_claims + missy_additional_claims

    # FA
    answer = missy_total_claims
    return answer