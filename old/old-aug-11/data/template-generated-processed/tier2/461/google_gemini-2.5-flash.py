def solve():
    """Index: 461.
    Returns: the total cost to copy and bind the manuscripts.
    """
    # L1
    num_pages = 400 # manuscript is 400 pages
    cost_per_page = 0.05 # $0.05 per page
    copying_cost_per_manuscript = num_pages * cost_per_page

    # L2
    num_copies = 10 # 10 copies
    total_copying_cost = num_copies * copying_cost_per_manuscript

    # L3
    binding_cost_per_manuscript = 5.00 # $5.00 per manuscript
    total_binding_cost = binding_cost_per_manuscript * num_copies

    # L4
    total_cost = total_copying_cost + total_binding_cost

    # FA
    answer = total_cost
    return answer