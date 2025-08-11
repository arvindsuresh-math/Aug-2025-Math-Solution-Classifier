def solve():
    """Index: 7203.
    Returns: the total number of cases of cat food sold.
    """
    # L1
    first_group_customers = 8 # The first 8 customers
    cases_per_customer_first_group = 3 # bought 3 cases each
    cases_first_group = first_group_customers * cases_per_customer_first_group

    # L2
    second_group_customers = 4 # The next four customers
    cases_per_customer_second_group = 2 # bought 2 cases each
    cases_second_group = second_group_customers * cases_per_customer_second_group

    # L3
    third_group_customers = 8 # The last 8 customers
    cases_per_customer_third_group = 1 # only bought 1 case each
    cases_third_group = third_group_customers * cases_per_customer_third_group

    # L4
    total_cases_sold = cases_first_group + cases_second_group + cases_third_group

    # FA
    answer = total_cases_sold
    return answer