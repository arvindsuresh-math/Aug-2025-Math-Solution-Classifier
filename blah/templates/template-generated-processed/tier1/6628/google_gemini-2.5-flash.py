def solve():
    """Index: 6628.
    Returns: the total number of paintings Tracy sold.
    """
    # L1
    first_customers = 4 # Four of those customers
    paintings_per_first_customer = 2 # bought two paintings each
    paintings_from_first_group = first_customers * paintings_per_first_customer

    # L2
    next_customers = 12 # The next 12 of those customers
    paintings_per_next_customer = 1 # bought one painting each
    paintings_from_next_group = next_customers * paintings_per_next_customer

    # L3
    last_customers = 4 # The last 4 customers
    paintings_per_last_customer = 4 # bought four paintings each
    paintings_from_last_group = last_customers * paintings_per_last_customer

    # L4
    total_paintings_sold = paintings_from_first_group + paintings_from_next_group + paintings_from_last_group

    # FA
    answer = total_paintings_sold
    return answer