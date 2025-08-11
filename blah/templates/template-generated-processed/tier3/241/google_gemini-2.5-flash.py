def solve():
    """Index: 241.
    Returns: the number of desktop computers sold.
    """
    # L1
    total_computers = 72 # total of 72 computers
    laptop_divisor = 2 # half of their sales
    laptops_sold = total_computers / laptop_divisor

    # L2
    netbook_divisor = 3 # one-third are netbooks
    netbooks_sold = total_computers / netbook_divisor

    # L3
    total_laptops_netbooks = laptops_sold + netbooks_sold

    # L4
    desktop_computers_sold = total_computers - total_laptops_netbooks

    # FA
    answer = desktop_computers_sold
    return answer