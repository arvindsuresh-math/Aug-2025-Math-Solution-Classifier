def solve():
    """Index: 4676.
    Returns: the total money Tim raised.
    """
    # L1
    max_donation = 1200 # maximum $1200 donation
    num_max_donors = 500 # 500 people
    max_donations_total = max_donation * num_max_donors

    # L2
    half_divisor = 2 # half this sum of money
    smaller_donation_amount = max_donation / half_divisor

    # L3
    times_factor = 3 # three times as many people
    num_smaller_donors = num_max_donors * times_factor

    # L4
    smaller_donations_total = num_smaller_donors * smaller_donation_amount

    # L5
    total_initial_donations = smaller_donations_total + max_donations_total

    # L6
    percentage_decimal = 0.4 # 40% of the total money
    total_money_raised = total_initial_donations / percentage_decimal

    # FA
    answer = total_money_raised
    return answer