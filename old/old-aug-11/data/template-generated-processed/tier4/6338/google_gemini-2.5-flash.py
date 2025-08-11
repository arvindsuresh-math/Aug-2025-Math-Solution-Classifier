def solve():
    """Index: 6338.
    Returns: the total amount Lisa will spend on her phone in the first year.
    """
    # L1
    phone_cost = 1000 # $1000
    case_percent_num = 20 # 20% of the cost of the phone
    percent_factor = 0.01 # WK
    case_cost = phone_cost * case_percent_num * percent_factor

    # L2
    headphones_divisor = 2 # half as much as the case
    headphones_cost = case_cost / headphones_divisor

    # L3
    contract_cost_per_month = 200 # $200/month
    months_per_year = 12 # WK
    contract_cost_year = contract_cost_per_month * months_per_year

    # L4
    total_spend = contract_cost_year + headphones_cost + case_cost + phone_cost

    # FA
    answer = total_spend
    return answer