def solve():
    """Index: 461.
    Returns: the total cost to have 10 copies of the manuscript copied and bound.
    """
    # L1
    num_pages = 400 # manuscript is 400 pages
    copy_cost_per_page = 0.05 # $0.05 per page to copy
    copy_cost_per_manuscript = num_pages * copy_cost_per_page

    # L2
    num_copies = 10 # 10 copies
    total_copy_cost = num_copies * copy_cost_per_manuscript

    # L3
    binding_cost_per_manuscript = 5.00 # $5.00 per manuscript to have it bound
    total_binding_cost = num_copies * binding_cost_per_manuscript

    # L4
    total_cost = total_copy_cost + total_binding_cost

    # FA
    answer = total_cost
    return answer