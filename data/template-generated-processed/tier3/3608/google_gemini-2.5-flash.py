def solve():
    """Index: 3608.
    Returns: the total number of customers in the group that arrived.
    """
    # L1
    num_offices = 3 # 3 local offices
    sandwiches_per_office = 10 # 10 bacon sandwiches
    office_sandwiches = num_offices * sandwiches_per_office

    # L2
    total_sandwiches_made = 54 # a total of 54 bacon sandwiches
    group_sandwiches = total_sandwiches_made - office_sandwiches

    # L3
    sandwiches_per_customer_in_group = 4 # 4 bacon sandwiches each
    customers_who_ordered = group_sandwiches / sandwiches_per_customer_in_group

    # L4
    half_group_multiplier = 2 # half of the group
    total_customers_in_group = customers_who_ordered * half_group_multiplier

    # FA
    answer = total_customers_in_group
    return answer