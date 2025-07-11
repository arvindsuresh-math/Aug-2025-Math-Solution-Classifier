def solve():
    """Index: 241.
    Returns: the number of desktop computers sold last month.
    """
    # L1
    total_computers = 72 # Mr. Lu's store was able to sell a total of 72 computers
    laptop_divisor = 2 # half of their sales are laptops
    laptops_sold = total_computers / laptop_divisor

    # L2
    netbook_divisor = 3 # one-third are netbooks
    netbooks_sold = total_computers / netbook_divisor

    # L3
    laptops_and_netbooks_sold = laptops_sold + netbooks_sold

    # L4
    desktop_computers_sold = total_computers - laptops_and_netbooks_sold

    # FA
    answer = desktop_computers_sold
    return answer