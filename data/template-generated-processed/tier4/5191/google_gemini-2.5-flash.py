def solve():
    """Index: 5191.
    Returns: the amount Paul earns from his parents.
    """
    # L1
    plates_count = 40 # plates from 40 different states
    total_us_states = 50 # WK
    proportion_of_plates = plates_count / total_us_states

    # L2
    percent_multiplier = 100 # WK
    percentage_of_plates = proportion_of_plates * percent_multiplier

    # L3
    earnings_per_percent_point = 2 # his parents will give him $2
    total_earnings = percentage_of_plates * earnings_per_percent_point

    # FA
    answer = total_earnings
    return answer