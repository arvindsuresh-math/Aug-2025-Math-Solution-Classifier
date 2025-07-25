def solve():
    """Index: 4521.
    Returns: the total amount John pays per year for EpiPens.
    """
    # L1
    months_per_year = 12 # WK
    epipen_frequency_months = 6 # every 6 months
    epipens_per_year = months_per_year / epipen_frequency_months

    # L2
    epipen_cost = 500 # $500
    insurance_coverage_percent = 0.75 # insurance covers 75%
    insurance_covered_amount = epipen_cost * insurance_coverage_percent

    # L3
    john_pays_per_epipen = epipen_cost - insurance_covered_amount

    # L4
    total_annual_payment = john_pays_per_epipen * epipens_per_year

    # FA
    answer = total_annual_payment
    return answer